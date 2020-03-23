from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='games'),
    path('accounts/signup/', views.signup, name='signup'),  
    path('games/create/', views.GameCreate.as_view(), name='games_create'), 
]