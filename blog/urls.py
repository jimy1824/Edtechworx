from django.urls import path
from blog import views

urlpatterns = [
    path('blogs_list/', views.BlogList.as_view() , name='blogs_list'),
    path('blog_detail/', views.BlogDetail.as_view() , name='blog_detail'),

]