from diet.models import Diet
from plan.models import Plan
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class PlanModelTest(TestCase):

    def make_plan(
        self,
        diet_plan='This is a test diet plan',
    ):
        return Plan.objects.create(
            diet=self.make_diet(),
            diet_plan=diet_plan,
        )

    def make_diet(
        self,
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
            user=self.make_user(),
        )

    def make_user(self):
        return User.objects.create_user(username='testuser', password='testpass')

    def test_create_plan_instance(self):
        plan = self.make_plan()
        plan.full_clean()
        plan.save()
        self.assertEqual(plan.diet_plan, 'This is a test diet plan')
