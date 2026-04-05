from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
        ]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class AdminRegisterSerializer(UserRegisterSerializer):
    secret_code = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [field for field in UserRegisterSerializer.Meta.fields] + [
            "secret_code"
        ]

    def validate_secret_code(self, value):
        if value != settings.ADMIN_REGISTRATION_SECRET_CODE:
            raise serializers.ValidationError("Invalid secret code.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("secret_code")

        user = User(**validated_data)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        return user
