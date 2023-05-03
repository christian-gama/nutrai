from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Patient(models.Model):
    """
    Patient model for a nutritionist's patient, extending the Django User model.
    This model includes fields for the patient's age, weight, height, dietary_restrictions, goals,
    and notes. The Patient class is meant to be used in conjunction with Django's built-in
    tools and ORM for managing patients in a nutritionist's practice.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(150)])
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, validators=[
        MinValueValidator(1.00)])
    height_m = models.DecimalField(max_digits=4, decimal_places=2, validators=[
        MinValueValidator(1.00)])

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
