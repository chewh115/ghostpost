from django.urls import path
from boo import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('submit/', views.submit, name='submit')
]