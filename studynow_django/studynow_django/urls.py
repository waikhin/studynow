from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/courses/', include('course.urls')),
    path('coursereco/', include('coursereco.urls')), 
    path('static/', serve, {'document_root': 'C:/Users/waikh/OneDrive/Desktop/StudyNow/studynow_vue/dist'}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

