from django.urls import path

from .views import (
    ProductStatisticsListAPIView,
    UserLessonDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView, CustomerProductsUpdateAPIView,
)

urlpatterns = [
    path('lesson-views/', ProductListAPIView.as_view(), name='lesson-views'),
    path('products/<int:pk>/lessons/', ProductDetailAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),
    # ---- create data for tests ----
    path('products/<int:pk>/lessons/<int:lesson_id>/update/', UserLessonDetailAPIView.as_view(), name='update-lesson'),
    path('customer-products/<int:pk>/', CustomerProductsUpdateAPIView.as_view(), name='customer-products'),
]
