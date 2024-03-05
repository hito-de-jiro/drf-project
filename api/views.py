from django.shortcuts import render
from rest_framework import generics

from api.models import Lesson, Product, User
from api.serializers import LessonSerializer, ProductSerializer, OwnerSerializer


def index(request):
    return render(request, 'index.html')


class LessonAPIList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class OwnerAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
