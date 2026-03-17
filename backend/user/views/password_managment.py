from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema)
from django.contrib.auth.password_validation import validate_password
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import ChangePasswordSerializer


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Change password",
        description="Change password.",
        request=ChangePasswordSerializer,
        responses={
            200: OpenApiResponse(
                description="Password changed.",
            ),
            400: OpenApiResponse(description="current password is wrong."),
            400: OpenApiResponse(description="new password is invalid."),
        },
        tags=["users"],
    )

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        current_password = serializer.validated_data["current_password"]
        new_password = serializer.validated_data["new_password"]

        if not user.check_password(current_password):
            return Response(
                {"details": "current password is wrong."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            validate_password(user=user, password=new_password)
        except ValidationError:
            return Response(
                {"details": "new password is invalid."},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.set_password(new_password)
        user.save()
        return Response(
            {"details": "password changed."},
            status=status.status.HTTP_200_OK
        )
    
