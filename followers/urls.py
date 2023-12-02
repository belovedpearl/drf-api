from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    #path('posts/<int:pk>/', views.PostDetail.as_view()),
]