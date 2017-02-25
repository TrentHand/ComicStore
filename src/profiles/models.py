from django.db import models

# Create your models here.

#profile is used to store the customers information
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')


    def __str__(self):
        return self.name