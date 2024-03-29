from django.urls import path

from .views import (
    ProductStatisticsListAPIView,
    LessonViewCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView
)

urlpatterns = [
    path('lesson-views/', ProductListAPIView.as_view(), name='lesson-views'),
    path('products/<int:pk>/lessons/', ProductDetailAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),
    # ---- update watched time ----
    path('update-lesson/', LessonViewCreateAPIView.as_view(), name='update-lesson'),
]
