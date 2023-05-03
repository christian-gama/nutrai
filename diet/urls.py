from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import DietViewSet

app_name = 'diet'

router = SimpleRouter()
router.register('diets', DietViewSet, basename='diet')

urlpatterns = [
    path('', include(router.urls)),
]
