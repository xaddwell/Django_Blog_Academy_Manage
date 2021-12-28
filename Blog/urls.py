"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from index import views as index_views
from acdlist import views as acdlist_views



urlpatterns = [
    path("", index_views.index_view),
    path('index', index_views.index_view),
    path('test', index_views.index_test),
    path('admin/', admin.site.urls),
    path('note/', include('note.urls')),
    path('user/', include('user.urls')),
    path('academy/', include('acdmpage.urls')),
    path('acdlist/', include('acdlist.urls')),
    path('statistic/', include(('statistic.urls', 'statistic'), namespace='statistic')),
    path('mdeditor/', include('mdeditor.urls'))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)