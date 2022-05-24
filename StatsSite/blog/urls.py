"""StatsSite URL Configuration

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
from django.urls import path
from .views import index,match_details, today_matchs, tomorrow_matchs, j2_matchs

urlpatterns = [
    path('', index, name="blog-index"),
    path('soccer-bet/', today_matchs, name="blog-today_matchs"),
    path('soccer-bet/tomorrow', tomorrow_matchs, name="blog-tomorrow_matchs"),
    path('soccer-bet/after-tomorrow', j2_matchs, name="blog-j2_matchs"),
    path("match-details/<str:slug>/", match_details, name="blog-match_details")
]
