from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('login/', views.login_me, name='login'),
    path('logout/', views.logout_me, name='logout'),
    path('delete/<int:id>/', views.delete_user, name='delete'),
]
