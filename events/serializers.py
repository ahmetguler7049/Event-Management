from rest_framework import serializers
from .models import Event, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category, created = Category.objects.get_or_create(name=category_data['name'])
            validated_data['category'] = category
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category, created = Category.objects.get_or_create(name=category_data['name'])
            instance.category = category
        return super().update(instance, validated_data)
