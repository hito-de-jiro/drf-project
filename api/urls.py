from django.urls import path

from .views import (
    LessonListAPIView,
    ProductLessonListAPIView,
    ProductStatisticsListAPIView,
    ProductListCreateAPIView,
    LessonCreateAPIView
)

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson-views-list'),
    path('products/<int:product_id>/lessons/', ProductLessonListAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),

    path('add-products/', ProductListCreateAPIView.as_view(), name='add-product'),
    path('add-lessons/', LessonCreateAPIView.as_view(), name='add-lesson'),
]
