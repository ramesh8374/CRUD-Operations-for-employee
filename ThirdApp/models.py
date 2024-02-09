from django.db import models

# Create your models here.
class UserTable(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    email_id = models.EmailField()

    def __str__(self):
        return self.name