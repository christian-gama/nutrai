from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

"""
This class represents a Diet model, which includes information about a specific diet plan.
It includes attributes such as the diet plan's name, description, duration, goals, allowed and
restricted foods, meal plan, nutritional information and cost.
This model can be used to represent any type of diet plan, such as a low-carb diet, vegan diet,
or Mediterranean diet.
"""


class Diet(models.Model):
    # Define choices for goals
    WEIGHT_LOSS = 'weight_loss'
    MUSCLE_GAIN = 'muscle_gain'
    HEALTHY_LIFESTYLE = 'healthy_lifestyle'
    GOALS_CHOICES = [
        (WEIGHT_LOSS, 'Weight Loss'),
        (MUSCLE_GAIN, 'Muscle Gain'),
        (HEALTHY_LIFESTYLE, 'Healthy Lifestyle'),
    ]

    # Define choices for meal plan
    VEGAN = 'vegan'
    KETO = 'keto'
    MEDITERRANEAN = 'mediterranean'
    MEAL_PLAN_CHOICES = [
        (VEGAN, 'Vegan'),
        (KETO, 'Keto'),
        (MEDITERRANEAN, 'Mediterranean'),
    ]

    # Define choices for nutritional info
    LOW_CALORIE = 'low_calorie'
    HIGH_PROTEIN = 'high_protein'
    LOW_FAT = 'low_fat'
    NUTRITIONAL_INFO_CHOICES = [
        (LOW_CALORIE, 'Low Calorie'),
        (HIGH_PROTEIN, 'High Protein'),
        (LOW_FAT, 'Low Fat'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    duration_in_weeks = models.IntegerField()
    goals = models.CharField(max_length=50, choices=GOALS_CHOICES)
    allowed_foods = models.TextField()
    restricted_foods = models.TextField()
    meal_plan = models.CharField(max_length=50, choices=MEAL_PLAN_CHOICES)
    nutritional_info = models.CharField(
        max_length=50, choices=NUTRITIONAL_INFO_CHOICES)
    cost_in_usd = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10000.0)])

    def __str__(self):
        return self.name
