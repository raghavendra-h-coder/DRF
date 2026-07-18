from logging import exception

from django.contrib.auth.models import User
from rest_framework import generics, status, serializers
from rest_framework.response import Response

from accounts.serializers import RegisterSerializer, LoginSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        return Response(
            {
                "message": "Login Successful",
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_200_OK
        )