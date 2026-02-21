from django.db import models
from  Guest.models import*
# Create your models here.


class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=30,null=True)
    complaint_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)