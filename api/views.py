from rest_framework import generics

from .models import LessonView
from .serializers import (
    LessonViewSerializer,
    LessonViewExtendedSerializer,
)


class LessonViewListAPIView(generics.ListAPIView):
    serializer_class = LessonViewSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = LessonView.objects.filter(user=user)
        return queryset


class ProductLessonViewListAPIView(generics.ListAPIView):
    serializer_class = LessonViewExtendedSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')
        queryset = LessonView.objects.filter(user=user,
                                             lesson__products__id=product_id)
        return queryset
