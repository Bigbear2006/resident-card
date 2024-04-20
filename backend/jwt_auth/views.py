from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import User


class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserInfoAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get(self, request: Request):
        return Response(self.serializer_class(request.user).data, 200)


class UpdateUserAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
