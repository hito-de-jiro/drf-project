from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response

from api.models import (
    Product,
    UserLesson,
    Lesson
)
from api.serializers import (
    LessonSerializer,
    ProductSerializer,
    UserLessonSerializer,
)


class UserLessonListAPIView(generics.ListAPIView):
    serializer_class = UserLessonSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserLesson.objects.filter(user=user)
        return queryset


# class UserLessonAPIList(generics.ListAPIView):
#     serializer_class = UserLessonSerializer
#     queryset = UserLesson.objects.all()


# class UserLessonAPIDetail(viewsets.ViewSet):
#     def list(self, request):
#         queryset = UserLesson.objects.all()
#         serializer = UserLessonSerializer(
#             queryset, many=True
#         )
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = UserLesson.objects.all()
#         lessons = get_object_or_404(queryset, pk=pk)
#         serializer = UserLessonSerializer(lessons)
#         return Response(serializer.data)


class LessonAPIList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class ProductAPIList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
