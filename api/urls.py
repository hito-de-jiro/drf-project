from django.urls import path

from .views import (
    ProductLessonListAPIView,
    ProductStatisticsListAPIView,
    # -----------------------
    ProductListCreateAPIView,
    LessonListCreateAPIView,
    UserLessonDetailAPIView,
    ProductListAPIView,
)

urlpatterns = [
    path('products/<int:product_id>/lessons/', ProductLessonListAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),
    # ---- create data for tests ----
    path('add-products/', ProductListCreateAPIView.as_view(), name='add-product'),
    path('add-lessons/', LessonListCreateAPIView.as_view(), name='add-lesson'),
    path('user-lesson-update/<int:pk>', UserLessonDetailAPIView.as_view(), name='update-lesson'),
    # ---- fixed ----
    path('lesson-views/', ProductListAPIView.as_view(), name='lesson-views'),
]
