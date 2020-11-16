from django.urls import path

from .class_views import (PostListView, PostDetailsView, AddPostView, UpdatePostView, DeletePostView)

urlpatterns = [
    path('', PostListView.as_view(), name='posts-list'),
    path('<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('add/',AddPostView.as_view(), name='add-post'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='edit-post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),

]