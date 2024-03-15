from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers

from .models import LessonView, Product, Lesson, UserProductAccess


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for user-related lessons"""
    class Meta:
        model = LessonView
        fields = ['id', 'lesson', 'watched_time_seconds', 'status']


class LessonExtendedSerializer(serializers.ModelSerializer):
    """Serializer for product-related and user-related lessons"""
    class Meta:
        model = LessonView
        fields = ['id', 'lesson', 'watched_time_seconds'
                                  'status', 'last_watched_time']


class ProductStatisticsSerializer(serializers.ModelSerializer):
    """Serializer for displaying statistics for all products"""
    total_watched_lessons = serializers.SerializerMethodField()
    total_watching_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    acquisition_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'total_watched_lessons', 'total_watching_time', 'total_students',
                  'acquisition_percentage']

    def get_total_watched_lessons(self, obj):
        return Lesson.objects.filter(products=obj).count()

    def get_total_watching_time(self, obj):
        total_time = LessonView.objects.filter(lesson__products=obj).aggregate(total_time=Sum('watched_time_seconds'))[
            'total_time']
        return total_time if total_time else 0

    def get_total_students(self, obj):
        return UserProductAccess.objects.filter(product=obj).count()

    def get_acquisition_percentage(self, obj):
        total_users = User.objects.count()
        access_count = obj.userproductaccess_set.count()
        return (access_count / total_users) * 100 if total_users > 0 else 0
