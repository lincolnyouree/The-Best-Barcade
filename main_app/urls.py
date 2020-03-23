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
    path('games/<int:bar_id>/add_game/', views.add_game, name='add_game'),
]