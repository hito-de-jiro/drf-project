from django.urls import path
from .views import (
    LessonAPIList,
    ProductAPIList,
)

urlpatterns = [
    path('lessons/', LessonAPIList.as_view(), name='lessons'),
    path('products/', ProductAPIList.as_view(), name='products'),

]

# /customers/{customer_pk}/products/
# /customers/{customer_pk}/products/{product_pk}/
# /customers/{customer_pk}/products/{product_pk}/lessons
