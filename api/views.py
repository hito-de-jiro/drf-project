from django.db.models import Q
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response

from .models import LessonView, Product
from .serializers import (
    ProductStatisticsSerializer,
    NewViewedLessonSerializer,
    ProductsSerializer,
    ProductDetailSerializer, CustomerProductsSerializer,
)


class ProductListAPIView(generics.ListAPIView):
    """List all products with lessons that the current user have permission"""
    serializer_class = ProductsSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.filter(product_lesson__isnull=False).distinct()
        # checking customer like owner
        queryset = queryset.filter(Q(customer=user) | Q(owner=user))

        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs.get('pk')
        try:
            queryset = Product.objects.filter(customer=user.id, id=pk, product_lesson__isnull=False).distinct()
        except Product.DoesNotExist:
            queryset = Product.objects.none()

        return queryset


class ProductStatisticsListAPIView(generics.ListAPIView):
    """Displaying for displaying statistics for all products"""
    queryset = Product.objects.all()
    serializer_class = ProductStatisticsSerializer


class UserLessonDetailAPIView(GenericAPIView, UpdateModelMixin):
    """Update lesson viewed information"""
    serializer_class = NewViewedLessonSerializer
    queryset = LessonView.objects.all()

    def get_object(self):
        user = self.request.user
        lesson_id = self.kwargs['pk']
        try:
            lesson_view = LessonView.objects.get(user=user, lesson=lesson_id)
            return lesson_view
        except LessonView.DoesNotExist:
            raise NotFound("Lesson not found")

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({"error": "LessonView does not exist for this user and lesson."},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CustomerProductsUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Update customer product"""
    serializer_class = CustomerProductsSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(id=self.kwargs['pk'])

        return queryset
