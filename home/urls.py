from django.urls import path
from home import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('home/', views.Home.as_view() , name='home')
]