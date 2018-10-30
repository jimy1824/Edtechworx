from django.conf.urls import url
from django.urls import path
from courses import views

urlpatterns = [
    path('courses_list/', views.CoursesList.as_view() , name='courses_list'),
    # path('course_detail/(?P<course_id>\d+)', views.CourseDetail.as_view() , name='course_detail')
    url(r'^course_detail/(?P<course_id>\d+)/',views.CourseDetail.as_view() , name='course_detail'),
    url(r'^course_enrollment/(?P<course_id>\d+)/',views.CoursesEnrollment.as_view() , name='course_enrollment'),
]