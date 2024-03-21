from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import LessonView, Product, Lesson
from .serializers import (
    ProductStatisticsSerializer,
    NewProductSerializer,
    NewLessonSerializer,
    NewViewedLessonSerializer,
    ProductsSerializer,
    ProductDetailSerializer,
)


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.filter(customer=user, lesson__isnull=False).distinct()

        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs.get('pk')
        try:
            queryset = Product.objects.filter(customer=user, id=pk, lesson__isnull=False).distinct()
        except Product.DoesNotExist:
            queryset = Product.objects.none()

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
        queryset = Lesson.objects.filter(products__owner=user)

        return queryset

    def perform_create(self, serializer):
        serializer.save()


class UserLessonDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = NewViewedLessonSerializer

    def get_queryset(self):
        user = self.request.user
        lesson_viewed_id = self.kwargs.get('pk')
        queryset = LessonView.objects.filter(user=user.id, lesson_id=lesson_viewed_id)

        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj
