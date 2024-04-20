from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from . import models, serializers, utils


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class EventViewSet(ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class CategoryEventViewSet(ModelViewSet):
    queryset = models.CategoryEvent.objects.all()
    serializer_class = serializers.CategoryEventSerializer


class HospitalViewSet(ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer


class BankViewSet(ModelViewSet):
    queryset = models.Bank.objects.all()
    serializer_class = serializers.BankSerializer


class CardViewSet(ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer

    @action(['GET'], False, 'pending')
    def get_pending_cards(self, request: Request):
        data = self.serializer_class(self.queryset.filter(status='Отправлена на рассмотрение'), many=True).data
        return Response(data, 200)


class BuyTicketAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TicketSerializer

    def post(self, request: Request):
        data = request['data']
        ticket = models.Ticket.objects.create(
            owner=request.user,
            event=data['event'],
        )
        return Response(self.serializer_class(ticket).data)


class VerifyPassportAPIView(GenericAPIView):
    serializer_class = serializers.PassportSerializer

    def post(self, request: Request):
        data = request.data
        valid = utils.check_password(data['series'], data['number'])
        return Response({'valid': valid}, 200)
