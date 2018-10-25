from django.urls import path
from gallery import views

urlpatterns = [
    path('gallery/', views.GalleryView.as_view() , name='gallery'),

]