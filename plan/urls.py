from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import PlanViewSet

app_name = 'plan'

router = SimpleRouter()
router.register(r'plans', PlanViewSet, basename='plans')

urlpatterns = [
    path('', include(router.urls)),
]
