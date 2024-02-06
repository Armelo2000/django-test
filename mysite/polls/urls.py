from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path("", views.index, name="index"),
    path("api/author/", AuthorUpdateView.as_view()),
    path('api/author/<int:pk>/', AuthorUpdateView.as_view()),

]