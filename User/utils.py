from google import genai
from django.conf import settings
import json
import re


class GeminiDesignGenerator:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate_plan(self, data):
        width = data.get("width")
        length = data.get("length")
        sqft = data.get("sqft")
        floors = data.get("floors", 1)
        shape = data.get("shape", "Rectangular")
        unit_type = data.get("unit_type", "2BHK")
        bedrooms = data.get("bedrooms", "2")
        bathrooms = data.get("bathrooms", "2")
        style = data.get("style", "Modern Premium")
        soil = data.get("soil", "Firm")
        kitchen_type = data.get("kitchen_type", "Open")
        budget = data.get("budget", "Standard")
        entrance = data.get("entrance", "Any")
        vastu = data.get("vastu", "Yes")
        parking = data.get("parking", "No")
        balcony = data.get("balcony", "No")
        puja_room = data.get("puja_room", "No")
        utility_area = data.get("utility_area", "No")
        dining = data.get("dining", "Yes")
        study_room = data.get("study_room", "No")
        prefs = data.get("prefs", "")

        area_info = f"{width} x {length} feet" if width and length else f"{sqft} square feet"

        prompt = f"""
You are an expert residential architect and estimator.

Generate a high-quality conceptual residential floor plan in STRICT JSON ONLY.

PROJECT INPUT:
- Plot size: {area_info}
- Plot shape: {shape}
- Floors: {floors}
- Unit type: {unit_type}
- Bedrooms needed: {bedrooms}
- Bathrooms needed: {bathrooms}
- Style: {style}
- Soil type: {soil}
- Kitchen type: {kitchen_type}
- Budget level: {budget}
- Entrance preference: {entrance}
- Vastu preference: {vastu}
- Parking: {parking}
- Balcony: {balcony}
- Puja room: {puja_room}
- Utility area: {utility_area}
- Dining required: {dining}
- Study/work room: {study_room}
- User notes: {prefs}

PLANNING RULES:
1. Create a practical residential layout.
2. No room overlap.
3. Use logical adjacency:
   - entrance -> foyer/living
   - living near dining
   - kitchen near dining
   - bedrooms in quieter/private zone
   - bathrooms accessible but private
4. Respect requested bedroom and bathroom count.
5. If dining is "No", merge dining into living if logical.
6. If parking is requested, include parking/car porch area.
7. If puja room is "Yes", include a compact puja room.
8. If utility area is "Yes", place it near kitchen.
9. If balcony is "Yes", place balcony near bedroom or living.
10. If study room is "Yes", include compact study/work room.
11. Prefer good ventilation and circulation.
12. If vastu is Yes, prefer East/North entrance when possible and logically align rooms.
13. Use realistic room sizes in feet.
14. Total built area should be reasonably consistent with the plot or sqft target.
15. Include only major usable spaces. Do not produce random tiny unusable rooms.

COORDINATE RULES:
- Each room must have:
  - name
  - x
  - y
  - w
  - h
- Use integer values only.
- x, y, w, h are in feet.
- No negative values.
- No overlap.
- Keep all rooms inside a reasonable rectangular plan boundary.

COST ESTIMATION RULES:
- Provide Indian residential conceptual cost estimate.
- Include these items where relevant:
  Foundation, RCC structure, brickwork, plastering, flooring, electrical, plumbing,
  doors/windows, painting, kitchen work, bathroom fittings, labor, contingency.
- Use budget-sensitive rates:
  Economy = lower range
  Standard = mid range
  Premium/Luxury = higher range
- Grand total must equal the sum of breakdown totals.

OUTPUT JSON FORMAT EXACTLY:
{{
  "project_profile": {{
    "plot_size": "{area_info}",
    "shape": "{shape}",
    "floors": {floors},
    "unit_type": "{unit_type}",
    "budget": "{budget}"
  }},
  "floor_plan": {{
    "rooms": [
      {{
        "name": "Living Room",
        "x": 0,
        "y": 0,
        "w": 12,
        "h": 14
      }}
    ],
    "total_built_area": 0,
    "planning_notes": [
      "string note 1",
      "string note 2"
    ]
  }},
  "cost_estimation": {{
    "breakdown": [
      {{
        "item": "Foundation",
        "qty": "1200 sqft basis",
        "rate": 250,
        "total": 300000
      }}
    ],
    "grand_total": 0
  }},
  "summary": "Explain zoning, privacy, circulation, ventilation, vastu handling, and budget logic in clear text."
}}

IMPORTANT:
- Return valid JSON only.
- No markdown.
- No explanation outside JSON.
"""

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            text = response.text.strip()
            json_text = re.sub(r"```json|```", "", text).strip()

            match = re.search(r"\{.*\}", json_text, re.DOTALL)
            if not match:
                return None

            parsed = json.loads(match.group())

            # Optional safety defaults
            if "floor_plan" not in parsed:
                parsed["floor_plan"] = {"rooms": [], "total_built_area": 0, "planning_notes": []}

            if "cost_estimation" not in parsed:
                parsed["cost_estimation"] = {"breakdown": [], "grand_total": 0}

            if "summary" not in parsed:
                parsed["summary"] = "Plan generated."

            return parsed

        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
            print("Raw response text:", text if 'text' in locals() else "No text")
            return None
        except Exception as e:
            print("Gemini error:", e)
            return None