from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='games'),
    path('accounts/signup/', views.signup, name='signup'),  
    path('bars/', views.bars_index, name='bars'),
    path('bars/bars_create', views.BarCreate.as_view(), name='bars_create'),
    path('bars/<int:bar_id>/', views.bar_details, name='bar_details'),
    path('bars/<int:bar_id>/create_game', views.GameCreate.as_view(), name='games_create')
]