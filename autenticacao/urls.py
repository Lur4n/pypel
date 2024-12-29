from django.urls import path
from . import views

app_name = 'auntenticacao'
urlpatterns = [
    path('', views.login, name='login'),
    path('get_perfis/', views.get_perfis, name='get_perfis'),
    path('logout/', views.logout, name='logout'),
]
