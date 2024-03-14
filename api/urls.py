from django.urls import path

from .views import (
    LessonViewListAPIView,
    ProductLessonViewListAPIView,
)

urlpatterns = [
    path('lesson-views/', LessonViewListAPIView.as_view(), name='lesson-views-list'),
    path('products/<int:product_id>/lesson-views/', ProductLessonViewListAPIView.as_view(),
         name='product-lesson-views-list'),
]
