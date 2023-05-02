from rest_framework import viewsets
from .models import Diet
from .serializers import DietSerializer


class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
