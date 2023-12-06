from django.db import models

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

class Login(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

class Books(models.Model):
    oname=models.CharField(max_length=20,null=True)  
    department = models.CharField(max_length=20)  
    event = models.CharField(max_length=40)
    date = models.DateField(max_length=20)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)