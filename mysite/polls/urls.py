from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path("", views.index, name="index"),
    path("api/musicians/", MusicianListView.as_view()),
    path('api/musicians/<int:pk>/', MusicianView.as_view()),
    path('api/albums/', AlbumListView.as_view()),
    path('api/albums/<int:pk>/', AlbumView.as_view()),
]