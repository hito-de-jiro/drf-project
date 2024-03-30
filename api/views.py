from django.db.models import Q
from rest_framework import generics, status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from .models import LessonView, Product, Lesson
from .serializers import (
    ProductStatisticsSerializer,
    ProductsSerializer,
    ProductDetailSerializer,
    LessonViewSerializer,
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
    """The product with lessons that the current user has permission"""
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs.get('pk')
        queryset = Product.objects.filter(id=pk, product_lesson__isnull=False).distinct()
        # checking customer like owner
        queryset = queryset.filter(Q(customer=user) | Q(owner=user), id=pk)

        return queryset


class ProductStatisticsListAPIView(generics.ListAPIView):
    """Displaying for displaying statistics for all products"""
    queryset = Product.objects.all()
    serializer_class = ProductStatisticsSerializer


class LessonViewCreateAPIView(UpdateAPIView):
    """Update watched time in the viewed lesson, only current user is allowed"""
    serializer_class = LessonViewSerializer

    def put(self, request, *args, **kwargs):
        lesson_id = int(request.data.get('lesson'))
        user = self.request.user
        time_watched = int(request.data.get('time_watched'))

        if not lesson_id or not time_watched:
            return Response({'message': 'Missing required data'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if user.product_customer.filter(product_lesson=lesson_id).exists():
                lesson_instance = Lesson.objects.get(pk=lesson_id)

                lesson_view, created = LessonView.objects.get_or_create(user=user, lesson=lesson_instance)
                lesson_view.time_watched = int(time_watched)
                lesson_view.save()

                serializer = LessonViewSerializer(lesson_view)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User does not have access to this lesson'},
                                status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
