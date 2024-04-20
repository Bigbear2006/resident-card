from rest_framework.serializers import ModelSerializer

from .models import User
from api.serializers import CardSerializer, TicketSerializer


class UserSerializer(ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'email', 'password', 'phone', 'birthday', 'passport_series',
            'passport_number', 'is_staff', 'cards', 'tickets',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
