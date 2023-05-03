from rest_framework import viewsets

from patient.permissions import PatientPermission
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.exceptions import PermissionDenied


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [PatientPermission]

    def perform_destroy(self, instance):
        if self.request.user.is_authenticated:
            instance.delete()
        else:
            raise PermissionDenied(
                "You must be logged in to delete objects.")
