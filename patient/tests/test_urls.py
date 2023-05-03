from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from ..views import PatientViewSet


class PatientURLsTest(APITestCase):

    def test_list_patients_url(self):
        url = reverse('patient:patient-list')
        self.assertEqual(resolve(url).func.cls, PatientViewSet)

    def test_patient_detail_url(self):
        url = reverse('patient:patient-detail', args=[1])
        self.assertEqual(resolve(url).func.cls, PatientViewSet)
