from django.urls import path
from . import views


urlpatterns = [
    path('', views.engineers, name="engineers"),
    path('file_engineer/<str:pk>/', views.file_engineer, name="file_engineer"),
]