"""
URL configuration for aitools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', views.ai_image_generation_view, name='ai-image-generation'),
    path('icon-generation/', views.icon_generation_view, name='icon-generation'),
    path('pdf-generation/', views.pdf_generation_view, name='pdf-generation'),
    path('video-generation/', views.video_generation_view, name='video-generation'),
    path('background-generation/', views.background_generation_view, name='background-generation'),
    path('background-removal/', views.background_removal_view, name='background-removal'),
    path('mockup-news/', views.mockup_news_view, name='mockup-news'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
