from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bettas/', views.bettas_index, name='index'),
    path('bettas/<int:betta_id>/', views.bettas_detail, name='detail')
]
