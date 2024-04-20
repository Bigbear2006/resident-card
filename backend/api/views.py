from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from . import models, serializers, utils


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class EventViewSet(ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class CreateCardAPIView(CreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer


class BuyTicketAPIView(GenericAPIView):
    serializer_class = serializers.TicketSerializer

    def post(self, request: Request):
        data = request['data']
        ticket = models.Ticket.objects.create(
            price=data.get('price', None),
            user=request.user,
            event=request.event,
        )
        return Response(self.serializer_class(ticket).data)


class VerifyPassportAPIView(GenericAPIView):
    serializer_class = serializers.PassportSerializer

    def post(self, request: Request):
        data = request.data
        valid = utils.check_password(data['series'], data['number'])
        return Response({'valid': valid}, 200)
