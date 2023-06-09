from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

app_name = 'patient'

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
]
