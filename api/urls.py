from django.urls import path

from .views import (
    ProductStatisticsListAPIView,
    ProductListCreateAPIView,
    LessonListCreateAPIView,
    UserLessonDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
)

urlpatterns = [
    path('lesson-views/', ProductListAPIView.as_view(), name='lesson-views'),
    path('products/<int:pk>/lessons/', ProductDetailAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),
    # ---- create data for tests ----
    path('add-products/', ProductListCreateAPIView.as_view(), name='add-product'),
    path('add-lessons/', LessonListCreateAPIView.as_view(), name='add-lesson'),
    path('user-lesson-update/<int:pk>', UserLessonDetailAPIView.as_view(), name='update-lesson'),
]
