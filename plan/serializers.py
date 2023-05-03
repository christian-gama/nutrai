from rest_framework import serializers

from diet.serializers import DietSerializer
from .models import Plan


class PlanSerializer(serializers.ModelSerializer):
    """
    This class represents the serializer for the Diet Plan model.
    """
    diet = DietSerializer(read_only=True)

    class Meta:
        model = Plan
        fields = ['id', 'diet', 'diet_plan']
