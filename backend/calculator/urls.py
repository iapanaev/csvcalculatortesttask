from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CalculatorTaskViewSet


router = DefaultRouter()
router.register(r'calculator_tasks', CalculatorTaskViewSet, basename='calculator_tasks')


urlpatterns = [
    path('', include(router.urls))
]
