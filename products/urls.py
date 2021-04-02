from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createfn, name='createpage'),
    path('<int:product_id>/', views.detailfn, name='detailpage'),
    path('<int:product_id>/upvote', views.upvotefn, name='upvotepage'),
]
