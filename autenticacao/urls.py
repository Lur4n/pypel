from django.urls import path
from . import views

app_name = 'auntenticacao'
urlpatterns = [
    path('', views.login, name='login')
]