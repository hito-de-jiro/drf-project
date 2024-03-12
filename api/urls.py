from django.urls import path
from .views import (
    LessonAPIList,
    ProductAPIList,
    UserLessonAPIList,
)

urlpatterns = [
    path('user-lessons/', UserLessonAPIList.as_view()),

    path('products/', ProductAPIList.as_view()),
    path('lessons/', LessonAPIList.as_view()),
]
