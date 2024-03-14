from rest_framework import serializers

from .models import LessonView


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ['id', 'lesson', 'watched_time_seconds', 'status']


class LessonViewExtendedSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonView
        fields = ['id', 'lesson', 'watched_time_seconds', 'status', 'last_watched_time']
