from rest_framework import serializers

from .models import Lesson, User, Product


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'
