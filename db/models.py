from django.db import models

# Create your models here.

class user_info(models.Model):
    user_name =  models.CharField(max_length=32)
    user_password = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255,null=True )
