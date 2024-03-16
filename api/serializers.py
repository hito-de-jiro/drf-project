from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers

from .models import LessonView, Product, Lesson, UserProductAccess


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        read_only_fields = ['username']


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product object"""
    owner = UserSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'owner']


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for Lesson object"""
    products = ProductSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['title', 'video_link', 'duration_seconds', 'products']


class LessonViewSerializer(serializers.ModelSerializer):
    """Serializer for user-related lessons"""

    class Meta:
        model = LessonView
        fields = ['lesson', 'watched_time_seconds', 'status']
        read_only_fields = ['status']


class LessonExtendedSerializer(serializers.ModelSerializer):
    """Serializer for product-related and user-related lessons"""
    lesson = LessonSerializer()

    class Meta:
        model = LessonView
        fields = ['lesson', 'watched_time_seconds',
                  'status', 'last_watched_time']
        read_only_fields = ['status', ]


class ProductStatisticsSerializer(serializers.ModelSerializer):
    """Serializer for displaying statistics for all products"""
    total_watched_lessons = serializers.SerializerMethodField()
    total_watching_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    acquisition_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['owner', 'name', 'total_watched_lessons', 'total_watching_time', 'total_students',
                  'acquisition_percentage']

    def get_total_watched_lessons(self, obj):
        return Lesson.objects.filter(products=obj).count()

    def get_total_watching_time(self, obj):
        total_time = LessonView.objects.filter(status='Watched').aggregate(total_time=Sum('watched_time_seconds'))[
            'total_time']
        return total_time if total_time else 0

    def get_total_students(self, obj):
        return UserProductAccess.objects.filter(product=obj).count()

    def get_acquisition_percentage(self, obj):
        total_users = User.objects.count()
        access_count = obj.userproductaccess_set.count()
        return round(((access_count / total_users) * 100), 2) if total_users > 0 else 0


""""create data for tests"""


class NewProductSerializer(serializers.ModelSerializer):
    """Serializer for Product and Lesson objects"""

    class Meta:
        model = Product
        fields = ['name', 'owner', 'lessons']
        read_only_fields = ['owner']

    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj):
        lessons = Lesson.objects.filter(products=obj)
        return LessonSerializer(lessons, many=True).data


class NewProductWithLessonSerializer(serializers.Serializer):
    """Serializer for creating new product with lesson"""

    name = serializers.CharField(max_length=255)
    lesson = LessonSerializer()

    def create(self, validated_data):
        lesson_data = validated_data.pop('lesson')
        product = Product.objects.create(name=validated_data['name'])
        Lesson.objects.create(product=product, **lesson_data)
        return product


class NewLessonSerializer(serializers.ModelSerializer):
    """Serializer for a new lesson"""
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Lesson
        fields = ['title', 'video_link', 'duration_seconds', 'products']


class NewViewedLessonSerializer(serializers.ModelSerializer):
    """Serializer for product-related and user-related lessons"""

    class Meta:
        model = LessonView
        fields = '__all__'
        read_only_fields = ['products', 'user', 'status']

        depth = 1

