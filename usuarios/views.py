from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def logout(request):

    auth.logout(request)

    return redirect('login_user')

def login_user(request):

    if request.user.is_authenticated:

        return redirect('meus_produtos')
    
    if request.method == 'POST':
        nick = request.POST.get('username')
        senha = request.POST.get('password')

        if Usuario.objects.filter(user__username=nick).exists():
            user = auth.authenticate(request, username=nick, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    return render(request, 'index.html')

def registro_user(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        nome = request.POST.get('first_name')
        nick = request.POST.get('username')
        senha = request.POST.get('password')
        senha_confirm = request.POST.get('conf_password')

        if senha != '':
            if senha == senha_confirm:
                if not Usuario.objects.filter(user__username=nick).exists():
                    if not Usuario.objects.filter(user__email=email).exists():

                        user = User.objects.create_user(username=nick, email=email,  password=senha, first_name=nome)
                        user.save()
                        Usuario(user=user).save()

                    return redirect('login_user')
            else:
                print('senhas nao batem')
        else:
            print('sem senha')

    return render(request, 'auth-register.html')

@login_required(login_url='login_user')
def perfil(request):

    usuario_perfil = Usuario.objects.get(user=request.user)
    usuario_atual =Usuario.objects.get(id=usuario_perfil.id)
    user = User.objects.get(id=usuario_perfil.user_id)

    if request.method == 'POST':
        nick = request.POST.get('username')
        nome = request.POST.get('first_name')
        email = request.POST.get('email')
        imagem = request.FILES.get('foto_perfil')
        senha = request.POST.get('password')
        senha_nova = request.POST.get('new_password')

        if not Usuario.objects.filter(user__username=nick).exists():
             if nick != None:user.username = nick
        if not Usuario.objects.filter(user__email=email).exists():
            if email != None:user.email = email
        if nome != None:user.first_name = nome
        if imagem != None:usuario_atual.foto_user = imagem

        usuario_atual.save()
        user.save()

        return redirect('dashboard')
   
    
    contex = {
        'user': usuario_perfil,
        'user_atual': usuario_atual,
    }

    return render(request, 'editar-usuario.html', contex)