from django.urls import path
from . import views

app_name = 'bookmarks'

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('add/', views.link_create, name='link_create'),
    path('<int:pk>/edit/', views.link_update, name='link_update'),
    path('<int:pk>/delete/', views.link_delete, name='link_delete'),
]
