from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novo_produto/', views.registrar_produtos, name='registrar_produtos'),
    path('meus_produtos/', views.meus_produtos, name='meus_produtos'),
    path('<id>/editar_produto/', views.editar_produto, name='editar_produto'),
    path('<id>/deletar_produto/', views.deletar_produto, name='deletar_produto'),
    path('categoria_save/', views.registrar_produtos, name='categoria_save')
]