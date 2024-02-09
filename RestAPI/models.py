from django.db import models

# Create your models here.
class UserRegister(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username