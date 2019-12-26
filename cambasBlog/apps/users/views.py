from django.contrib.auth import get_user_model, logout
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import (UserSerializer, RegisterUserSerializer,
                          LoginSerializer, AuthorSerializer)

User = get_user_model()


class LoginAPI(generics.GenericAPIView):
    """Login in the system"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_200_OK)


class LogoutAPI(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        Token.objects.filter(user=user).delete()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateUserView(generics.CreateAPIView):
    """create new user and token in the system"""
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


class AuthorListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
