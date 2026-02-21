from django.db import models
from Admin.models import*
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to="Assets/User")
    user_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_civilengineering(models.Model):
    civileng_name=models.CharField(max_length=30)
    civileng_email=models.CharField(max_length=30)
    civileng_contact=models.CharField(max_length=30)
    civileng_address=models.CharField(max_length=30)
    civileng_photo=models.FileField(max_length=30)
    civileng_proof=models.FileField(max_length=30)
    civileng_password=models.CharField(max_length=30)
    place_id=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    civileng_status = models.IntegerField(default=0)