from rest_framework.serializers import ModelSerializer

from .models import User
from api.serializers import CardSerializer, TicketSerializer


class UserSerializer(ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'phone', 'birthday', 'passport_series',
            'passport_number', 'is_staff', 'cards', 'tickets',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            password=validated_data.pop('password'),
            **validated_data
        )
