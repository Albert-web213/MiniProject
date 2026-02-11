from django.shortcuts import render

# Create your views h ere.


def Sum(request):
    if request.method == "POST":
        a = int(request.POST.get("txt_number1"))
        b = int(request.POST.get("txt_number2"))
        c = a + b
        return render(request,"Basics/Sum.html",{'result':c})
    else:
        return render(request,"Basics/Sum.html")


def Calculator(request):
    if  request.method == "POST":
        a=int(request.POST.get("txt_name"))
        b=int(request.POST.get("txt1_name"))
        btn =  request.POST.get("btn_op")
        if btn == "+" :
            c = a + b
        elif btn == "-":
            c = a - b
        elif btn == "*":
            c = a*b                                         
        elif btn == "/":
            c = a/b
        return render(request,"Basics/Calculator.html",{'result':c})
    else:
        return render(request,"Basics/Calculator.html")
def Largest(request):
    if request.method == "POST":
        a=int(request.POST.get("txt_name"))
        b=int(request.POST.get("txt_name2"))
        if a>b:
            largest=a
        else:
            largest=b
        return render(request,"Basics/Largest.html",{'result':largest})
    else:
        return render(request,"Basics/Largest.html")
    
def Marklist(request):
    if request.method == "POST":
       FirstName=request.POST.get("txt_name")
       LastName=request.POST.get("txt1name")
       Department=request.POST.get("sel_Dept")
       Course=request.POST.get("sel_Course")
       Mark1=int(request.POST.get("txt_mark1"))
       Mark2=int(request.POST.get("txt_mark2"))
       Mark3=int(request.POST.get("txt_mark3"))
       Name=FirstName+LastName
       Mark=Mark1+Mark2+Mark3
       Percentage=(Mark/150)*100
       if Percentage>90:
           Grade="A+"
       elif Percentage > 30 and Percentage<=60:
            Grade="A"
       elif Percentage<30:
            Grade="B"       
       return render(request,"Basics/Marklist.html",{'Name':Name,'Department':Department,'Course':Course,'Mark':Mark,'Percentage':Percentage,'Grade':Grade})
    else:
        return render(request,"Basics/Marklist.html")

  
