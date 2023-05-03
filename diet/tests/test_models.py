from django.forms import ValidationError
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Diet


class DietModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='test_password')

    def test_create_diet_instance(self):
        diet = self.make_diet()
        diet.full_clean()
        diet.save()
        self.assertEqual(diet.name, 'Test Diet')

    def test_invalid_cost_in_usd(self):
        with self.assertRaises(ValidationError):
            diet = self.make_diet(cost_in_usd=-1.0)
            diet.full_clean()

    def test_invalid_duration_in_weeks(self):
        with self.assertRaises(ValidationError):
            diet = self.make_diet(duration_in_weeks=-1)
            diet.full_clean()

    def test_invalid_goals(self):
        with self.assertRaises(ValidationError):
            diet = self.make_diet(goals='invalid_goal')
            diet.full_clean()

    def test_invalid_meal_plan(self):
        with self.assertRaises(ValidationError):
            diet = self.make_diet(meal_plan='invalid_meal_plan')
            diet.full_clean()

    def test_invalid_nutritional_info(self):
        with self.assertRaises(ValidationError):
            diet = self.make_diet(nutritional_info='invalid_nutritional_info')
            diet.full_clean()

    def test_name_max_length(self):
        name = 'a' * 151
        with self.assertRaises(ValidationError):
            diet = self.make_diet(name=name)
            diet.full_clean()

    def test_description_max_length(self):
        description = 'a' * 501
        with self.assertRaises(ValidationError):
            diet = self.make_diet(description=description)
            diet.full_clean()

    def test_str_method(self):
        diet = self.make_diet()
        self.assertEqual(str(diet), 'Test Diet')

    def make_diet(self,
                  name='Test Diet',
                  description='A test diet for testing purposes.',
                  duration_in_weeks=4,
                  goals=Diet.WEIGHT_LOSS,
                  allowed_foods='Fruits, Vegetables, Whole Grains',
                  restricted_foods='Processed Foods, Refined Sugar, Saturated Fats',
                  meal_plan=Diet.VEGAN,
                  nutritional_info=Diet.LOW_CALORIE,
                  cost_in_usd=49.99,
                  ):

        return Diet.objects.create(
            name=name,
            description=description,
            duration_in_weeks=duration_in_weeks,
            goals=goals,
            allowed_foods=allowed_foods,
            restricted_foods=restricted_foods,
            meal_plan=meal_plan,
            nutritional_info=nutritional_info,
            cost_in_usd=cost_in_usd,
            user=self.user
        )
