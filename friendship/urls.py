from django.urls import path

from friendship import views


urlpatterns = [
    path('users-list/', views.UserListView.as_view()),
    path('request/', views.RquestView.as_view()),
    path('request-list/', views.RequestListView.as_view()),
    path('accept/', views.AcceptView.as_view()),
    path('friends/', views.FriendListView.as_view())
]

