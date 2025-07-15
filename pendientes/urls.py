from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pendientes_index'),
    path('solo_ids/', views.solo_ids, name='solo_ids'),
    path('ids_titles/', views.ids_titles, name='ids_titles'),
    path('no_resueltos/', views.no_resueltos, name='no_resueltos'),
    path('resueltos/', views.resueltos, name='resueltos'),
    path('ids_user/', views.ids_user, name='ids_user'),
    path('resueltos_user/', views.resueltos_user, name='resueltos_user'),
    path('no_resueltos_user/', views.no_resueltos_user, name='no_resueltos_user'),
]
