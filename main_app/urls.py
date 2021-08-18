from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bettas/', views.bettas_index, name='index'),
    path('bettas/<int:betta_id>/', views.bettas_detail, name='detail'),
    path('bettas/create/', views.BettaCreate.as_view(), name='bettas_create'),
    path('bettas/<int:pk>/update', views.BettaUpdate.as_view(), name='bettas_update'),
    path('bettas/<int:pk>/delete', views.BettaDelete.as_view(), name='bettas_delete'),
]
