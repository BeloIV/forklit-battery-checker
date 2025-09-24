from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ForkliftViewSet, BatteryViewSet, ChargeSessionViewSet, UserMeView

router = DefaultRouter()
router.register("forklifts", ForkliftViewSet)
router.register("batteries", BatteryViewSet)
router.register("charges", ChargeSessionViewSet)

urlpatterns = [
    path("me/", UserMeView.as_view()),
    path("", include(router.urls)),
]