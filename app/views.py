from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from app.models import Categoria, Contato, Produto, Compra
from app.forms import FormCategoria, FormContato, ProdutoForm, FormUsuario, FormEditarUsuario


def index(request):
    return render(request, 'index.html')


def quemSomos(request):
    membros = [
        {'nome': 'Lucas Bombonato', 'cargo': 'Desenvolvedor', 'foto': 'img/lucas-bombonato.jpg'},
        {'nome': 'Julia Nunes', 'cargo': 'Desenvolvedora', 'foto': 'img/julia-nunes.jpg'},
    ]
    return render(request, 'quem-somos.html', {'membros': membros})


def loja(request):
    produtos = Produto.objects.all()
    return render(request, 'loja.html', {'produtos': produtos})


def cadastrarUsuario(request):
    formulario = FormUsuario(request.POST or None)
    if request.method == 'POST':
        if formulario.is_valid():
            usuario = formulario.save()
            grupo_cliente, _ = Group.objects.get_or_create(name="Cliente")
            usuario.groups.add(grupo_cliente)
            return redirect('login')
    return render(request, 'cadastro.html', {'form': formulario})


def loginUsuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html')


def logoutUsuario(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def editarUsuario(request):
    formulario = FormEditarUsuario(request.POST or None, instance=request.user)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('editarusuario')
    compras = Compra.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'edit-usuario.html', {'form': formulario, 'compras': compras})


@login_required(login_url='login')
def comprarProduto(request, id_prod):
    if request.method != 'POST':
        return redirect('loja')

    produto = get_object_or_404(Produto, id=id_prod)
    if produto.quantidade <= 0:
        messages.error(request, 'Esta key está sem estoque no momento.')
        return redirect('loja')

    produto.quantidade -= 1
    produto.save()

    Compra.objects.create(
        usuario=request.user,
        produto=produto,
        produto_nome=produto.nome,
        quantidade=1,
        valor_total=produto.preco,
    )

    messages.success(request, f'Compra de {produto.nome} finalizada com sucesso.')
    return redirect('editarusuario')


@login_required
@staff_member_required
def listarCategoria(request):
    _categorias = Categoria.objects.all().values()
    return render(request, 'categoria.html', {'categorias': _categorias})


@login_required
@staff_member_required
def delCategoria(request, id_cat):
    _categoria = Categoria.objects.get(id=id_cat)
    _categoria.delete()
    return redirect('categoria')


@login_required
@staff_member_required
def addCategoria(request):
    formulario = FormCategoria(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')
    return render(request, 'add-categoria.html', {'form': formulario})


@login_required
@staff_member_required
def editCategoria(request, id_cat):
    _categoria = Categoria.objects.get(id=id_cat)
    formulario = FormCategoria(request.POST or None, instance=_categoria)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('categoria')
    return render(request, 'edit-categoria.html', {'form': formulario})


@login_required
@staff_member_required
def listarContato(request):
    contatos = Contato.objects.all()
    return render(request, 'contato.html', {'contatos': contatos})


@login_required
@staff_member_required
def delContato(request, id_contato):
    _contato = Contato.objects.get(id=id_contato)
    _contato.delete()
    return redirect('contato')


def addContato(request):
    formulario = FormContato(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Mensagem enviada com sucesso.')
            return redirect('addcontato')
    return render(request, 'add-contato.html', {'form': formulario})


@login_required
@staff_member_required
def listarProduto(request):
    _produtos = Produto.objects.all()
    return render(request, 'produto.html', {'produtos': _produtos})


@login_required
@staff_member_required
def addProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produto')
    else:
        form = ProdutoForm()
    return render(request, 'add-produto.html', {'form': form})


@login_required
@staff_member_required
def editProduto(request, id_prod):
    _produto = get_object_or_404(Produto, id=id_prod)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=_produto)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('produto')
    return render(request, 'edit-produto.html', {'form': form, 'produto': _produto})


@login_required
@staff_member_required
def delProduto(request, id_prod):
    _produto = get_object_or_404(Produto, id=id_prod)
    _produto.delete()
    return redirect('produto')


@login_required
@staff_member_required
def dashboard(request):
    total_produtos = Produto.objects.count()
    total_categorias = Categoria.objects.count()
    total_contatos = Contato.objects.count()
    total_usuarios = User.objects.count()
    total_compras = Compra.objects.count()
    return render(request, 'dashboard.html', {
        'total_produtos': total_produtos,
        'total_categorias': total_categorias,
        'total_contatos': total_contatos,
        'total_usuarios': total_usuarios,
        'total_compras': total_compras,
    })


@login_required
@staff_member_required
def listarUsuarios(request):
    usuarios = User.objects.all().order_by('date_joined')
    return render(request, 'usuarios.html', {'usuarios': usuarios})


@login_required
@staff_member_required
def editUsuarioAdmin(request, id_user):
    _usuario = get_object_or_404(User, id=id_user)
    formulario = FormEditarUsuario(request.POST or None, instance=_usuario)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios')
    return render(request, 'edit-usuario-admin.html', {'form': formulario, 'usuario': _usuario})


@login_required
@staff_member_required
def delUsuario(request, id_user):
    _usuario = get_object_or_404(User, id=id_user)
    _usuario.delete()
    return redirect('usuarios')
