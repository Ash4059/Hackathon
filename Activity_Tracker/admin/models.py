from django.db import models

class Admin(models.Model):
    Email_id=models.EmailField(max_length=30)
    Password=models.CharField(max_length=20)
