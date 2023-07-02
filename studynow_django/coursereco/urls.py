from django.urls import path
from .views import RecommendCourse

urlpatterns = [
    path('api/recommend/', RecommendCourse.as_view()),
]
