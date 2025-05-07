from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("topics/", views.getTopics),
    path("rooms/", views.getRooms),
    path("rooms/<int:id>", views.getSingleRoom),
    path("rooms/<int:id>/messages", views.getRoomMessages),
]