from rest_framework import serializers

from .models import Lesson, Customer, Product, Owner


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'duration', 'status_watched', 'last_watched', 'product']


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'owner', 'name', 'description', 'lessons']


class CustomerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = ['username', 'products']
