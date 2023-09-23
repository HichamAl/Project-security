from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class VerifiedUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    uploaded_file = models.FileField(upload_to='uploads/', default='default_file.txt')


    def __str__(self):
        return  self.user.username

