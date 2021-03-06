from django.contrib import admin
from django.urls import path, include
# from . import views
import products.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.home, name = 'firsthomepage'),
    path('accounts/', include('accounts.urls') ),
    path('products/', include('products.urls') ),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
