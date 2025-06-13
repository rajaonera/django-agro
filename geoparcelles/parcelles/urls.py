from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParcelleViewSet

router = DefaultRouter()
router.register(r'parcelles', ParcelleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
