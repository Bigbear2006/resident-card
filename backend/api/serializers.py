from rest_framework.serializers import ModelSerializer, Serializer, PrimaryKeyRelatedField, CharField

from . import models


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title', 'events')
        depth = 1

    def to_representation(self, instance):
        data = super(CategorySerializer, self).to_representation(instance)
        data['events'] = EventWithoutCategoriesSerializer(instance.events, many=True).data
        return data


class EventWithoutCategoriesSerializer(ModelSerializer):
    class Meta:
        model = models.Event
        exclude = ('categories',)


class CategoryEventSerializer(ModelSerializer):
    class Meta:
        model = models.CategoryEvent
        fields = '__all__'


class EventSerializer(ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'
        depth = 1


class CardSerializer(ModelSerializer):
    class Meta:
        model = models.Card
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.update(owner=user)
        return super(CardSerializer, self).create(validated_data)


class TicketSerializer(ModelSerializer):
    event = PrimaryKeyRelatedField(queryset=models.Event.objects.all())

    class Meta:
        model = models.Ticket
        fields = '__all__'
        depth = 1


class PassportSerializer(Serializer):
    series = CharField()
    number = CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = '__all__'


class BankSerializer(ModelSerializer):
    class Meta:
        model = models.Bank
        fields = '__all__'
