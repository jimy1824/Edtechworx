from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.Contact.as_view() , name='contact'),

]