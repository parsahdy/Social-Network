from django.urls import path

from posts import views

urlpatterns = [
    path('post/', views.PostView.as_view(), name='post'),
    path('post/<int:post_pk>/', views.PostView.as_view(), name='post'),
    path('post-list/', views.PostListView.as_view(), name='post-list'),
]