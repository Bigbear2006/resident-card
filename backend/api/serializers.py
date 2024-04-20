from rest_framework.serializers import ModelSerializer

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


class EventSerializer(ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'
        depth = 1


class CardSerializer(ModelSerializer):
    class Meta:
        model = models.Card
        fields = '__all__'
