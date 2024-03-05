from django.urls import path

from .views import (
    index,
    LessonAPIList,
    OwnerAPIList,
    ProductAPIList,
    ProductAPIUpdate,
    ProductAPIDestroy
)

urlpatterns = [
    path('index/', index, name='index'),
    path('lessons/', LessonAPIList.as_view(), name='list_lessons'),
    path('users/', OwnerAPIList.as_view(), name='list_owners'),
    path('products-list/', ProductAPIList.as_view(), name='list_products'),
    path('products-update/<int:pk>/', ProductAPIUpdate.as_view(), name='update_products'),
    path('products-destroy/<int:pk>/', ProductAPIDestroy.as_view(), name='destroy_products'),
]
