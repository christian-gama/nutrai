from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from ..views import DietViewSet


class DietURLsTest(APITestCase):

    def test_list_diets_url(self):
        url = reverse('diet:diet-list')
        self.assertEqual(resolve(url).func.cls, DietViewSet)

    def test_diet_detail_url(self):
        url = reverse('diet:diet-detail', args=[1])
        self.assertEqual(resolve(url).func.cls, DietViewSet)
