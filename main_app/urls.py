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
    path('bettas/<int:betta_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('bettas/<int:betta_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('accounts/signup/', views.signup, name='signup'),
]
