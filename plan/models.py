from django.db import models

from diet.models import Diet


class Plan(models.Model):
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    diet_plan = models.TextField()

    def __str__(self):
        return f'{self.diet.name} Plan'
