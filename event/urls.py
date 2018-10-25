from django.urls import path
from event import views
from  django.conf.urls import url

urlpatterns = [
    path('events_list/', views.EventsList.as_view() , name='events_list'),
    # path('event_detail/', views.EventDetail.as_view() , name='event_detail'),
    url(r'^event_detail/(?P<event_id>\d+)/',views.EventDetail.as_view() , name='course_detail'),

]