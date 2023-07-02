from django.urls import path

from course import views

urlpatterns = [
    path('', views.get_courses),
    path('get_frontpage_courses/', views.get_frontpage_courses),
    path('get_categories/', views.get_categories),
    path('<slug:slug>/', views.get_course),
]
