from django.urls import path

from .views import (
    index,
    LessonAPIList,
    UserAPIList,
    ProductAPIList,
    ProductAPIUpdate,
    ProductAPIDestroy,
    OwnerAPIList,
    UserAPIUpdate,
    UserAPIDestroy,
    LessonAPIUpdate
)

urlpatterns = [
    path('index/', index, name='index'),
    path('owners/', OwnerAPIList.as_view(), name='owners'),
    path('products/', ProductAPIList.as_view(), name='products'),
    path('products/<int:pk>/', ProductAPIUpdate.as_view(), name='update_products'),
    path('products/<int:pk>/', ProductAPIDestroy.as_view(), name='destroy_products'),
    path('products/<int:pk>/lessons/', LessonAPIList.as_view(), name='lessons'),
    path('products/<int:pk>/lessons/<int:id>/', LessonAPIUpdate.as_view(), name='update_user'),
    path('users/', UserAPIList.as_view(), name='users'),
    path('users/<int:pk>/', UserAPIUpdate.as_view(), name='update_user'),
    path('users/<int:pk>/', UserAPIDestroy.as_view(), name='destroy_user'),

]
