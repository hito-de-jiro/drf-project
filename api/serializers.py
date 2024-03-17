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
        fields = ['id', 'product_name', 'owner']


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for Lesson object"""
    products = ProductSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['products', 'lesson_title', 'lesson_link', 'lesson_duration', ]


class LessonViewSerializer(serializers.ModelSerializer):
    """Serializer for user-related lessons"""

    class Meta:
        model = LessonView
        fields = ['lesson', 'time_watched', 'status_watched']
        read_only_fields = ['status_watched']


class LessonExtendedSerializer(serializers.ModelSerializer):
    """Serializer for product-related and user-related lessons"""
    lesson = LessonSerializer()

    class Meta:
        model = LessonView
        fields = ['lesson', 'watched_time',
                  'status_watched', 'last_watched']
        read_only_fields = ['status_watched', ]


class ProductStatisticsSerializer(serializers.ModelSerializer):
    """Serializer for displaying statistics for all products"""
    watched_lessons = serializers.SerializerMethodField()
    watched_time = serializers.SerializerMethodField()
    customer_count = serializers.SerializerMethodField()
    product_purchase = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_name', 'watched_lessons', 'watched_time', 'customer_count',
                  'product_purchase']

    def get_watched_lessons(self, obj):
        return Lesson.objects.filter(products=obj).count()

    def get_watched_time(self, obj):
        total_time = LessonView.objects.filter(status=True).aggregate(total_time=Sum('watched_time_seconds'))[
            'total_time']
        return total_time if total_time else 0

    def get_customer_count(self, obj):
        return UserProductAccess.objects.filter(product=obj).count()

    def get_product_purchase(self, obj):
        total_users = User.objects.count()
        access_count = obj.userproductaccess_set.count()
        return round(((access_count / total_users) * 100), 2) if total_users > 0 else 0


""""create data for tests"""


class NewProductSerializer(serializers.ModelSerializer):
    """Serializer for Product and Lesson objects"""

    class Meta:
        model = Product
        fields = ['product_name', 'owner', 'lessons']
        # fields = '__all__'
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
        fields = ['lesson_title', 'lesson_link', 'lesson_duration', 'products', ]


class NewViewedLessonSerializer(serializers.ModelSerializer):
    """Serializer for product-related and user-related lessons"""

    class Meta:
        model = LessonView
        fields = '__all__'
        read_only_fields = ['products', 'status', 'user', 'lesson']


class ProductsLessonSerializer(serializers.ModelSerializer):
    """Displaying """
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_name']
        

    def get_product_name(self, product):
        lessons = product.lesson
        lesson_data = []
        try:
            lesson_view = LessonView.objects.get(user=self.context['request'].user, lesson=lessons)
            status_watched = lesson_view.status_watched == 'Watched'
            time_watched = lesson_view.time_watched
        except LessonView.DoesNotExist:
            status_watched = False == 'Not watched'
            time_watched = 0
        #
        lesson_dict = {
            'lesson_title': lessons.lesson_title,
            'lesson_link': lessons.lesson_link,
            'lesson_duration': lessons.lesson_duration,
            'time_watched': time_watched,
            'status_watched': status_watched
        }
        lesson_data.append(lesson_dict)

        name_product = product.lesson.lesson_title
        print(product.lesson)

        return {name_product: lesson_dict}
