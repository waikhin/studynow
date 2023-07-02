

# Create your views here.
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course, Category
from .serializers import CourseListSerializer, CategorySerializer

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def get_frontpage_courses(request):
    courses = Course.objects.all() [0:4]
    serializer = CourseListSerializer(courses, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many= True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    serializer = CourseListSerializer(course)
    return Response(serializer.data)