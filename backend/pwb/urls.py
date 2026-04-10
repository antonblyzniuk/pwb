from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ping, PWBUnitViewSet


router = DefaultRouter()
router.register("pwbunits", PWBUnitViewSet, "pwbunit")

urlpatterns = [
        path("ping/", ping, name="ping"),
        path("", include(router.urls)),
]
