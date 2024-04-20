from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import User


class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserInfoAPIView(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get(self, request: Request):
        return Response(self.serializer_class(request.user).data, 200)
        # return Response(self.serializer_class(User.objects.get(id=1)).data, 200)
