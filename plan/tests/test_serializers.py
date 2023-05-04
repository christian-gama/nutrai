from django.test import TestCase
from ..models import Plan
from ..serializers import PlanSerializer
from diet.models import Diet
from django.contrib.auth.models import User


class PlanSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='testpassword')

        self.diet = Diet.objects.create(
            user=self.user,
            name='Test Diet',
            description='Test diet description',
            duration_in_weeks=4,
            goals='Weight Loss',
            allowed_foods='Chicken, vegetables, fruits',
            restricted_foods='Sweets, soda, fast food',
            meal_plan='Keto',
            nutritional_info='Low Fat',
            cost_in_usd=100
        )

        self.plan = Plan.objects.create(
            diet=self.diet,
            diet_plan='This is a test diet plan'
        )

    def test_plan_serializer(self):
        serialized_data = PlanSerializer(instance=self.plan).data
        self.assertEqual(serialized_data['id'], self.plan.id)
        self.assertEqual(serialized_data['diet_plan'], self.plan.diet_plan)

        deserialized_data = {
            'diet': self.plan.diet.id,
            'diet_plan': 'This is another test diet plan'
        }
        serializer = PlanSerializer(data=deserialized_data)
        self.assertTrue(serializer.is_valid())
        plan_instance = serializer.save(diet=self.plan.diet)
        self.assertEqual(plan_instance.diet, self.plan.diet)
        self.assertEqual(plan_instance.diet_plan,
                         deserialized_data['diet_plan'])
