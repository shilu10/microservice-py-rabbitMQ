from django.urls import path 
from . import views

urlpatterns = [
    path("get/", views.get_products),
    path("<str:id>/", views.post_likes),
]