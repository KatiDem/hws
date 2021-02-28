"""blog_project URL Configuration

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
from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('product/delete', ProductDeleteView.as_view()),
    path('product/update', ProductUpdateView.as_view()),
    path('product/list', ProductListView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/delete', CategoryDeleteView.as_view()),
    path('category/update', CategoryUpdateView.as_view()),
    path('category/list', CategoryListView.as_view()),
    path('comment/create', CommentCreateView.as_view()),
    path('comment/delete', CommentDeleteView.as_view()),
    path('comment/update', CommentUpdateView.as_view()),
    path('comment/list', CommentListView.as_view()),

]
