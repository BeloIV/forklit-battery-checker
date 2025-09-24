from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Forklift, Battery, ChargeSession

class ForkliftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forklift
        fields = "__all__"

class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = "__all__"

class ChargeSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeSession
        fields = "__all__"
        read_only_fields = ["user"]

class UserMeSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "groups"]