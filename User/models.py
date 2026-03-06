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


class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_plane_file=models.FileField(upload_to="Assests/Request/")
    request_doc=models.FileField(upload_to="Assest/Request/")
    request_status=models.IntegerField(default=0)
    request_reply=models.CharField(max_length=30,null=True)
    request_description=models.CharField(max_length=30)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    civileng_id=models.ForeignKey(tbl_civilengineering,on_delete=models.CASCADE)
