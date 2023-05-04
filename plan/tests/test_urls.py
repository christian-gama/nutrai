from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from ..views import PlanViewSet


class PlanURLsTest(APITestCase):

    def test_list_diets_url(self):
        url = reverse('plan:plans-list')
        self.assertEqual(resolve(url).func.cls, PlanViewSet)

    def test_diet_detail_url(self):
        url = reverse('plan:plans-detail', args=[1])
        self.assertEqual(resolve(url).func.cls, PlanViewSet)
