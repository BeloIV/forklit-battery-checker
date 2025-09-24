from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Forklift, Battery, ChargeSession
from .serializers import (
    ForkliftSerializer, BatterySerializer, ChargeSessionSerializer, UserMeSerializer
)

class ForkliftViewSet(viewsets.ModelViewSet):
    queryset = Forklift.objects.all()
    serializer_class = ForkliftSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class BatteryViewSet(viewsets.ModelViewSet):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer
    permission_classes = [permissions.DjangoModelPermissions]

class ChargeSessionViewSet(viewsets.ModelViewSet):
    queryset = ChargeSession.objects.select_related("battery", "user").all()
    serializer_class = ChargeSessionSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserMeView(generics.GenericAPIView):
    serializer_class = UserMeSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response(self.get_serializer(request.user).data)