"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from some_app.views import index
from some_app.views import index as ix, process_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('some_app/', include('some_app.urls')),
    path('cw20/', include('cw20.urls')),
    path('cw21/', include('cw21.urls')),
    path('cw22/', include('cw21.urls'))
]
