"""webapi_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from posts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ApiRoot.as_view(),name=views.ApiRoot.name),
    path('profiles/',views.ProfileList.as_view(),name=views.ProfileList.name),
    path('profiles/<int:pk>/',views.ProfileDetail.as_view(),name=views.ProfileDetail.name),
    path('profile-posts/',views.ProfilePost.as_view(),name=views.ProfilePost.name),
    path('posts/',views.PostList.as_view(),name=views.PostList.name),
    path('posts/<int:pk>',views.PostDetail.as_view(),name=views.PostDetail.name),
    path('comments/',views.CommentList.as_view(),name=views.CommentList.name),
    path('comments/<int:pk>',views.CommentDetail.as_view(),name=views.CommentDetail.name),
    path('posts-comments/',views.PostComment.as_view(),name=views.PostComment.name),
    path('users/',views.UserList.as_view(),name=views.UserList.name),
    path('users/<int:pk>',views.UserDetail.as_view(),name=views.UserDetail.name),
]
