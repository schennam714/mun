"""tjmun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('awards/', include('tjmun.apps.awards.urls', namespace = 'awards')),
    path('techmun/', include('tjmun.apps.techmun.urls', namespace = 'techmun')),
    path('auth/', include('tjmun.apps.auth.urls', namespace = 'auth')),
    path('', include('tjmun.apps.home.urls', namespace='home')),
    path('', include('social_django.urls', namespace = 'social')),
    path('members/', include('tjmun.apps.users.urls', namespace = 'users')),

]
if settings.DEBUG:
    urlpatterns.extend(static("static/", document_root=settings.STATIC_ROOT))
    urlpatterns.extend(static("media/", document_root = settings.MEDIA_ROOT))
