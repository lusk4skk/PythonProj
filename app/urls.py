from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),

    # Paginas publicas
    path('quem-somos/', views.quemSomos, name="quemsomos"),
    path('quem-somos', views.quemSomos),
    path('loja/', views.loja, name="loja"),
    path('loja', views.loja),

    # Usuario
    path('cadastro/', views.cadastrarUsuario, name="cadastro"),
    path('cadastro', views.cadastrarUsuario),
    path('login/', views.loginUsuario, name="login"),
    path('login', views.loginUsuario),
    path('editar-usuario/', views.editarUsuario, name="editarusuario"),
    path('editar-usuario', views.editarUsuario),

    # Categoria
    path('Categoria/', views.listarCategoria, name="categoria"),
    path('Categoria', views.listarCategoria),
    path('del-categoria/<int:id_cat>/', views.delCategoria, name="delcategoria"),
    path('del-categoria/<int:id_cat>', views.delCategoria),
    path('add-categoria/', views.addCategoria, name="addcategoria"),
    path('add-categoria', views.addCategoria),
    path('edit-categoria/<int:id_cat>/', views.editCategoria, name="editcategoria"),
    path('edit-categoria/<int:id_cat>', views.editCategoria),

    # Contato
    path('contato/', views.listarContato, name="contato"),
    path('contato', views.listarContato),
    path('del-contato/<int:id_contato>/', views.delContato, name="delcontato"),
    path('del-contato/<int:id_contato>', views.delContato),
    path('add-contato/', views.addContato, name="addcontato"),
    path('add-contato', views.addContato),

    # Produto
    path('add-produto/', views.addProduto, name="addproduto"),
    path('add-produto', views.addProduto),
    path('produto/', views.listarProduto, name="produto"),
    path('produto', views.listarProduto),
    path('comprar/<int:id_prod>/', views.comprarProduto, name="comprarproduto"),
    path('comprar/<int:id_prod>', views.comprarProduto),
    path('remover-compra/<int:id_compra>/', views.removerCompra, name="removercompra"),
    path('remover-compra/<int:id_compra>', views.removerCompra),
    path('edit-produto/<int:id_prod>/', views.editProduto, name="editproduto"),
    path('edit-produto/<int:id_prod>', views.editProduto),
    path('del-produto/<int:id_prod>/', views.delProduto, name="delproduto"),
    path('del-produto/<int:id_prod>', views.delProduto),

    # Avaliações
    path('avaliar/<int:id_compra>/', views.avaliarCompra, name="avaliarcompra"),
    path('avaliar/<int:id_compra>', views.avaliarCompra),

    # Dashboard
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard', views.dashboard),
    path('dashboard/usuarios/', views.listarUsuarios, name="usuarios"),
    path('dashboard/usuarios', views.listarUsuarios),
    path('dashboard/usuarios/edit/<int:id_user>/', views.editUsuarioAdmin, name="editusuarioadmin"),
    path('dashboard/usuarios/edit/<int:id_user>', views.editUsuarioAdmin),
    path('dashboard/usuarios/del/<int:id_user>/', views.delUsuario, name="delusuario"),
    path('dashboard/usuarios/del/<int:id_user>', views.delUsuario),
    path('dashboard/avaliacoes/', views.listarAvaliacoes, name="avaliacoesadmin"),
    path('dashboard/avaliacoes', views.listarAvaliacoes),
    path('dashboard/avaliacoes/del/<int:id_aval>/', views.delAvaliacao, name="delavaliacao"),
    path('dashboard/avaliacoes/del/<int:id_aval>', views.delAvaliacao),
]
