from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', views.ProfileDetailAPIView.as_view(), name='profile-detail'),
]
