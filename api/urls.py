from django.urls import path

from .views import (
    LessonListAPIView,
    ProductLessonListAPIView,
    ProductStatisticsListAPIView,
    # -----------------------
    ProductListCreateAPIView,
    LessonListCreateAPIView,
    UserLessonDetailAPIView,
    ProductsLessonAPIView,
)

urlpatterns = [
    path('lesson-views/', LessonListAPIView.as_view(), name='lesson-views'),
    path('products/<int:product_id>/lessons/', ProductLessonListAPIView.as_view(),
         name='product-lesson-views-list'),
    path('product-statistics/', ProductStatisticsListAPIView.as_view(),
         name='product-statistics-list'),
    # ---- create data for tests ----
    path('add-products/', ProductListCreateAPIView.as_view(), name='add-product'),
    path('add-lessons/', LessonListCreateAPIView.as_view(), name='add-lesson'),
    path('user-lesson-update/<int:pk>', UserLessonDetailAPIView.as_view(), name='update-lesson'),
    path('products-lessons/', ProductsLessonAPIView.as_view(), name='product-lessons'),
]
