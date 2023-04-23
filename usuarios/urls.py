from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout'),
    path('novo_user/', views.registro_user, name='registro_user'),
    path('perfil/', views.perfil, name='perfil')
]