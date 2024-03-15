from django.urls import path

from .views import (
    LessonListAPIView,
    ProductLessonListAPIView,
    ProductStatisticsListAPIView,
)

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson-views-list'),
    path('products/<int:product_id>/lessons/', ProductLessonListAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),
]
