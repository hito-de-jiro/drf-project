from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LessonAPIList,
    ProductAPIList,
    UserLessonListAPIView,
    # UserLessonAPIList,
    # UserLessonAPIDetail,
)


# lessons = UserLessonAPIDetail.as_view({'get': 'list'})
# lesson = UserLessonAPIDetail.as_view({'get': 'retrieve'})
#
# router = DefaultRouter()
# router.register(r'customer-lessons', UserLessonAPIDetail, basename='lesson')

urlpatterns = [
    # path('customer-lessons/', include(router.urls)),
    # path('user-lessons/', UserLessonAPIList.as_view()),

    path('user-lessons/', UserLessonListAPIView.as_view()),

    path('products/', ProductAPIList.as_view()),
    path('lessons/', LessonAPIList.as_view()),
]
