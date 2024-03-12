from rest_framework import serializers

from .models import Lesson, UserLesson, Product


class LessonSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True, read_only=True)
    products_lessons = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['title', 'url', 'duration', 'product', 'products_lessons']


class ProductSerializer(serializers.ModelSerializer):
    products_lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'products_lessons']
        depth = 1


class UserLessonSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = UserLesson
        fields = ['lesson', 'time_watched', 'status_watched', 'product']
        depth = 1
        read_only_fields = ['lesson', 'time_watched', 'status_watched', ]
