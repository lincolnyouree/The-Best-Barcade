from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),  
    path('bars/', views.bars_index, name='bars'),
    path('bars/bars_create', views.BarCreate.as_view(), name='bars_create'),
    path('bars/<int:pk>/update', views.BarUpdate.as_view(), name='bars_update'),
    path('bars/<int:bar_id>/', views.bar_details, name='bar_details'),
    path('bars/<int:bar_id>/games_create', views.GameCreate.as_view(), name='games_create'),
    path('bars/<int:pk>/delete', views.BarDelete.as_view(), name='bars_delete'),
    path('games/', views.games_index, name='games'),
    path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
    path('games/<int:game_id>', views.game_details, name='game_details'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'),
]