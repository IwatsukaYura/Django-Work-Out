from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    height = models.FloatField()
    weight = models.FloatField()

    REQUIRED_FIELDS = ["height", "weight"]

    def get_bmi(self):
        return self.weight / ((self.height / 100) * (self.height / 100))