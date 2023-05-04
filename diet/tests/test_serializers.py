from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from ..models import Diet
from ..serializers import DietSerializer


class DietSerializerTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='test_password')

        self.diet = Diet.objects.create(
            name='Test Diet',
            description='A test diet for testing purposes.',
            duration_in_weeks=4,
            goals=Diet.WEIGHT_LOSS,
            allowed_foods='Fruits, Vegetables, Whole Grains',
            restricted_foods='Processed Foods, Refined Sugar, Saturated Fats',
            meal_plan=Diet.VEGAN,
            nutritional_info=Diet.LOW_CALORIE,
            cost_in_usd=49.99,
            user=self.user
        )

        self.serializer = DietSerializer(instance=self.diet)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ['id', 'name', 'description', 'duration_in_weeks', 'goals',
             'allowed_foods', 'restricted_foods', 'meal_plan', 'nutritional_info', 'cost_in_usd']
        )

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.diet.name)

    def test_description_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['description'], self.diet.description)

    def test_duration_in_weeks_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['duration_in_weeks'],
                         self.diet.duration_in_weeks)

    def test_goals_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['goals'], self.diet.goals)

    def test_allowed_foods_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['allowed_foods'], self.diet.allowed_foods)

    def test_restricted_foods_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['restricted_foods'], self.diet.restricted_foods)

    def test_meal_plan_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['meal_plan'], self.diet.meal_plan)

    def test_nutritional_info_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['nutritional_info'], self.diet.nutritional_info)

    def test_cost_in_usd_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['cost_in_usd'], self.diet.cost_in_usd)

    def test_serialized_data_is_valid(self):
        data = self.serializer.data
        new_serializer = DietSerializer(data=data)
        self.assertTrue(new_serializer.is_valid())

    def test_serialized_data_creates_new_diet(self):
        data = self.serializer.data
        new_serializer = DietSerializer(data=data)
        new_serializer.is_valid()
        new_diet = new_serializer.save(user=self.user)
        self.assertIsNotNone(new_diet)
        self.assertEqual(new_diet.name, self.diet.name)
        self.assertEqual(new_diet.description, self.diet.description)
        self.assertEqual(new_diet.duration_in_weeks,
                         self.diet.duration_in_weeks)
        self.assertEqual(new_diet.goals, self.diet.goals)
