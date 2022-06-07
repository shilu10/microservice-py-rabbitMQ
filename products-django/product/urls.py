from django.urls import path 
from . import views
urlpatterns = [
    path("list/", views.list),
    path("create/", views.create),
    path("list/<str:id>", views.retrieve),
    path("delete/<str:id>", views.delete),
    path("update/<str:id>", views.update),
    path("users/", views.get_users),
    ]