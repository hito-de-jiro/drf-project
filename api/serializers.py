from rest_framework import serializers

from .models import Lesson, Owner, Product, User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    watched_lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('owner', 'name', 'description', 'lessons')
