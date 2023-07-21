from django.db import models


# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length=100, blank=True, null=False)
    user_email = models.EmailField(max_length=255, blank=True, null=False)
    user_password = models.CharField(max_length=50, blank=True, null=False)
