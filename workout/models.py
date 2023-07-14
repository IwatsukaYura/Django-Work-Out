from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    height = models.FloatField()
    weight = models.FloatField()

    REQUIRED_FIELDS = ["height", "weight"]

    def get_bmi(self):
        return self.weight / ((self.height / 100) * (self.height / 100))
    
    


class BodyPart(models.Model):
    part_num = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Training(models.Model):
    part_num = models.ForeignKey(BodyPart, on_delete=models.CASCADE, related_name='training')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name