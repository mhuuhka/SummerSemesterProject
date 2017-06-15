"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^login/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^threads/', include('app.urls')),
    url(r'^music/', include('app.urls')),
    url(r'^currency/', include('app.urls')),
    url(r'^movies/', include('app.urls')),
    url(r'^love/', include('app.urls')),
    url(r'^education/', include('app.urls')),
    url(r'^development/', include('app.urls'))
]
