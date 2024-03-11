from rest_framework import generics

from api.models import (
    Product,
    Customer,
    Lesson
)
from api.serializers import (
    LessonSerializer,
    ProductSerializer,
    CustomerSerializer,
)


class LessonAPIList(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class ProductAPIList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CustomerAPIList(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
