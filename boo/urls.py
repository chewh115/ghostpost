from django.urls import path
from boo import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('submit/', views.submit, name='submit'),
    path('boasts/', views.index, name='boasts'),
    path('roasts/', views.index, name='roasts'),
    path('upvote/<int:post_id>/', views.up_vote, name='upvote'),
    path('downvote/<int:post_id>/', views.down_vote, name='downvote')
]