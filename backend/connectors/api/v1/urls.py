from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137724ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137724", Testconnectors137724ViewSet, basename="testconnectors137724"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
