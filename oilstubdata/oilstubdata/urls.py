"""oilstubdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from oilandgasdata import views

admin.site.enable_nav_sidebar = False


urlpatterns = [
    path('api/v1/search/', views.SearchViewSet.as_view(), name='search'),
    path('oilandgasdata/', include(('oilandgasdata.urls', 'oilandgasdata'), namespace='oilandgasdata')),
    path(rf'home', admin.site.urls),
]
