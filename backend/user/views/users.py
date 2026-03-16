from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserRetrieveSerializer


class MyInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserRetrieveSerializer(request.user).data
        return Response(user, status=status.HTTP_200_OK)
