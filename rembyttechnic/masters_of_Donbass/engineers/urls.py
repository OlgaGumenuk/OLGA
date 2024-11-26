from django.urls import path
from . import views


urlpatterns = [
    path('', views.engineers, name="engineers"),
    path('file_engineer/<str:pk>/', views.file_engineer, name="file_engineer"),
    path('login/', views.login_engineer, name="login"),
    path('logout/', views.logout_engineer, name="logout"),
    path('register/', views.register_engineer, name="register"),
    path('account/', views.engineer_account, name="account"),
    path('edit-account/', views.edit_account, name="edit-account"),
]