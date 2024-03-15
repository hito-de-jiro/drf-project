from rest_framework import generics

from .models import LessonView, Product
from .serializers import (
    LessonViewSerializer,
    LessonExtendedSerializer,
    ProductStatisticsSerializer,
    NewProductSerializer,
    NewLessonSerializer,
)


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


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """Displaying and create for new products"""
    serializer_class = NewProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

    def get_queryset(self):
        queryset = Product.objects.filter(owner=self.request.user)
        return queryset


class LessonCreateAPIView(generics.ListCreateAPIView):
    """Displaying and create for new lessons"""
    serializer_class = NewLessonSerializer

