from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowersListView.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view()),
]