from django.urls import path
from blog import views
from  django.conf.urls import url
urlpatterns = [
    path('blogs_list/', views.BlogList.as_view() , name='blogs_list'),
    # path('blog_detail/', views.BlogDetail.as_view() , name='blog_detail'),
    url(r'^blog_detail/(?P<blog_id>\d+)/', views.BlogDetail.as_view(), name='blog_detail'),

]