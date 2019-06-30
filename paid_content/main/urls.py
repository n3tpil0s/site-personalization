"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from articles import views
from articles.views import HomeView, PaidView, ArticleListView, ArticleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='login.html',
                                     authentication_form=AuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    # path('articles/', views.show_articles, name='articles'),
    path('article/<pk>/', ArticleView.as_view(), name='article'),
    # url(r'^articles/(?P<id>[0-9]+)/', views.show_article, name='article'),
    path('subscribe-paid/', PaidView.as_view(), name='subscribe_paid')
]
