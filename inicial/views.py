from django.shortcuts import render, redirect
from . models import Produto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario

@login_required(login_url='login_user')
def dashboard(request):

    produtos = Produto.objects.all()
    user_atual = Usuario.objects.get(user=request.user)
    usuario_atual =Usuario.objects.get(id=user_atual.id)

    search = request.GET.get('search')
    if search:
        produtos = produtos.filter(name__icontains=search)

    page = request.GET.get('page', 1)
    paginator = Paginator(produtos,6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    ultimo = 0
    for i in produtos:
        ultimo = produtos.get(id=i.id)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        'produtos': result,
        'pagina_num': page_obj,
        'ultimo': ultimo,
        'user_atual': usuario_atual,
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='login_user')
def editar_produto(request, id):

    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco = request.POST.get('preco_produto')
        imagem = request.FILES.get('imagem_produto')
        descricao = request.POST.get('exampleFormControlTextarea1')
        categoria = request.POST.get('basicSelect')

        if nome != None:produto.name = nome
        if email != None:produto.email = email
        if preco != None:produto.price = preco
        if imagem != None:produto.foto_produto = imagem
        if descricao != None:produto.description = descricao
        if categoria != None:produto.categoria = categoria
        
        produto.save()

        return redirect('meus_produtos')

    context = {
        'produto': produto
    }

    return render(request, 'editar-produto.html', context)

@login_required(login_url='login_user')
def meus_produtos(request):

    produtos = Produto.objects.filter(usuario__user__username=request.user)
    user_atual = Usuario.objects.get(user=request.user)
    usuario_atual =Usuario.objects.get(id=user_atual.id)

    search = request.GET.get('search')
    if search:
        produtos = produtos.filter(name__icontains=search)

    page = request.GET.get('page', 1)
    paginator = Paginator(produtos,6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        'produtos': result,
        'pagina_num': page_obj,
        'user_atual': usuario_atual,
    }
    
    return render(request, 'meus-produtos.html', context)

@login_required(login_url='login_user')
def registrar_produtos(request):
    
    if request.method == 'POST':
        nome = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco = request.POST.get('preco_produto')
        imagem = request.FILES.get('imagem_produto')
        descricao = request.POST.get('exampleFormControlTextarea1')
        categoria = request.POST.get('basicSelect')

        produto = Produto(
            name = nome,
            email = email,
            price = preco,
            foto_produto = imagem,
            description = descricao,
            categoria = categoria,
            usuario = Usuario.objects.get(user__username=request.user)
        )
        
        produto.save()

        return redirect('meus_produtos')

    return render(request, 'registrar-produtos.html')

@login_required(login_url='login_user')
def deletar_produto(request, id):

    produto = Produto.objects.get(id=id)
    produto.delete()

    return redirect('meus_produtos')