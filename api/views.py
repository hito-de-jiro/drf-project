from rest_framework import generics

from .models import LessonView, Product, Lesson
from .serializers import (
    LessonViewSerializer,
    LessonExtendedSerializer,
    ProductStatisticsSerializer,
    NewProductSerializer,
    NewLessonSerializer, NewViewedLessonSerializer, )


class LessonListAPIView(generics.ListAPIView):
    """Displaying for user-related lessons"""
    serializer_class = LessonViewSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = LessonView.objects.filter(user=user)
        return queryset


class ProductLessonListAPIView(generics.ListAPIView):
    """Displaying for product-related and user-related lessons"""
    serializer_class = LessonExtendedSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')
        queryset = LessonView.objects.filter(user=user,
                                             lesson__products__id=product_id)
        return queryset


class ProductStatisticsListAPIView(generics.ListAPIView):
    """Displaying for displaying statistics for all products"""
    queryset = Product.objects.all()
    serializer_class = ProductStatisticsSerializer


"""create data for tests"""


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """Displaying and create for new products"""
    serializer_class = NewProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

    def get_queryset(self):
        queryset = Product.objects.filter(owner=self.request.user)
        return queryset


class LessonListCreateAPIView(generics.ListCreateAPIView):
    """Displaying and create for new lessons"""
    serializer_class = NewLessonSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        queryset = Lesson.objects.filter(products__owner=user)

        return queryset

    def perform_create(self, serializer):
        serializer.save()


class UserLessonDetailAPIView(generics.UpdateAPIView):
    serializer_class = NewViewedLessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')
        queryset = LessonView.objects.filter(user=user,
                                             lesson__products__id=product_id)
        return queryset
