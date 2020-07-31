from django.urls import path
from . import views

urlpatterns = [
    path('signUp/', views.sign_up, name = 'sign_up'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]