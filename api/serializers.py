from rest_framework import serializers

from .models import Lesson, UserLesson, Product


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    products_lessons = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['owner_id', 'name', 'products_lessons']
        depth = 1


# class UserLessonSerializer(serializers.ModelSerializer):
#     # product_name = ProductSerializer(many=True, read_only=True)
#     lessons = LessonSerializer(many=True)
#
#     class Meta:
#         model = UserLesson
#         # fields = '__all__'
#         fields = ['lessons', 'title', 'time_watched', 'status_watched', ]
#         # depth = 2


class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = '__all__'
