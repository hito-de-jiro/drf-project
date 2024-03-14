from django.urls import path

from .views import (
    LessonViewListAPIView,
    ProductLessonViewListAPIView,
    ProductStatisticsListAPIView,
)

urlpatterns = [
    path('lesson-views/', LessonViewListAPIView.as_view(), name='lesson-views-list'),
    path('product/<int:product_id>/lesson-views/', ProductLessonViewListAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),
]
