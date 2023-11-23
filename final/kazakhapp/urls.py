"""final URL Configuration

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
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main,  name='main'),
    path('art/', views.art, name='art'),
    path('traditions/', views.trad, name='trad'),
    path('sport/', views.sport, name='sport'),
    path('medicine/', views.medicine, name='med'),
    path('explore/' , views.explore, name='explore'),
    path('sign_up/' , views.adduser, name='sign'),
    path('data_loading/' , views.data_loading, name='loading'),
    path('upload/', views.upload, name = 'upload'),
    path('main/update/<int:comment_id>', views.update, name='update'),
    path('main/delete/<int:comment_id>', views.delete, name='delete'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('index/' , views.index, name='index'),
]
