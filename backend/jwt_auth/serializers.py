from rest_framework.serializers import ModelSerializer

from .models import User
from api.serializers import CardSerializer


class UserSerializer(ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
