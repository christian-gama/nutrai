from rest_framework import viewsets, status
from rest_framework.response import Response

from diet.models import Diet
from .models import Plan
from .serializers import PlanSerializer
from .permissions import PlanPermission
from .services import generate_diet_plan


class PlanViewSet(viewsets.ModelViewSet):
    """
    This class represents the viewset for the Diet Plan model.
    It provides actions such as create, retrieve, update, and destroy.
    """

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [PlanPermission]

    def get_queryset(self):
        return Plan.objects.filter(diet__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        This method generates a diet plan for the given diet.
        """

        id = request.data.get('diet_id')

        if not id:
            return Response({'error': 'Diet ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            diet = Diet.objects.get(pk=id, user=request.user)
        except Diet.DoesNotExist:
            return Response({'error': 'Diet not found.'}, status=status.HTTP_404_NOT_FOUND)

        diet_plan = generate_diet_plan(diet)
        serializer = PlanSerializer(
            data={'diet': diet.id, 'diet_plan': diet_plan})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        return Response(
            {'error': 'Updating plans is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(
            {'error': 'Updating plans is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
