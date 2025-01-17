from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Employee(AbstractUser):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    designation = models.CharField(max_length=50)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []