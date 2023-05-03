from rest_framework import viewsets

from .models import Diet
from .serializers import DietSerializer
from .permissions import DietPermission


class DietViewSet(viewsets.ModelViewSet):
    """
    This class represents the viewset for the Diet model.
    It provides actions such as create, retrieve, update, and destroy.
    """

    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    permission_classes = [DietPermission]

    def get_queryset(self):
        return Diet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
