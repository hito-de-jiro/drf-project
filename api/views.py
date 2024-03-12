from rest_framework import generics

from api.models import (
    Product,
    UserLesson,
    Lesson
)
from api.serializers import (
    LessonSerializer,
    ProductSerializer,
    UserLessonSerializer,
)


class UserLessonAPIList(generics.ListAPIView):
    serializer_class = UserLessonSerializer
    queryset = UserLesson.objects.all()


class LessonAPIList(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class ProductAPIList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
