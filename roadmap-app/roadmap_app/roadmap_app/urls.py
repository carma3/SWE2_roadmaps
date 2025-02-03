"""
URL configuration for roadmap_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from roadmaps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("roadmaps/", views.roadmap_list, name="roadmap_list"),
    path("roadmaps/create-roadmap-form", views.create_roadmap_form, name="create_roadmap_form"),
    path("create-roadmap/", views.create_roadmap, name="create_roadmap")
]

# Path syntax: path(URL route pattern, view function that should handle request, unique identifier (optional))