from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class customeruser(AbstractUser):
    age=models.IntegerField(null=True,blank=True,default=18)