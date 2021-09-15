from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cctv_data, name='get_cctv_data'), #response main page
    path('upload/', views.set_cctv_image, name='set_cctv_image'), #save image file to server
]