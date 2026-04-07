from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Health check",
    description="Returns API health status",
    tags=["health"]
)
@api_view(["GET"])
def ping(reqeust):
    return Response({"ping": "pong"}, status=status.HTTP_200_OK)

