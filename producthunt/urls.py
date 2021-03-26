from django.contrib import admin
from django.urls import path
# from . import views
import products.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.home, name = 'firsthomepage'),
]
