from rest_framework import serializers
from .models import Diet


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['id', 'name', 'description', 'duration_in_weeks', 'goals', 'allowed_foods',
                  'restricted_foods', 'meal_plan', 'nutritional_info', 'cost_in_usd']
