from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from . import models, serializers


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class EventViewSet(ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class CreateCardAPIView(CreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer


class VerifyPassportAPIView(APIView):
    def post(self, request: Request):
        return Response({'valid': True}, 200)
