from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name = 'loginpage'),
    path('signup', views.signup, name = 'signuppage'),
    path('logout', views.logout, name = 'logoutpage'),
]
