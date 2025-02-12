from django.urls import path
from .views import home, room, criarRoom, editarRoom, deletarRoom, loginPag, logoutUsuario, registrarUsuario, deletarMensagem, perfilUser, editarUsuario, topicosPesquisados, atvsRecentes

urlpatterns = [
    path('login/', loginPag, name='pagina-login'),
    path('logout/', logoutUsuario, name='pagina-logout'),
    path('registrar/', registrarUsuario, name='pagina-registro'),
    path('', home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('criar-sala/', criarRoom, name='criar-sala' ),
    path('editar-sala/<int:pk>/', editarRoom, name='editar-sala' ),
    path('deletar-sala/<int:pk>/', deletarRoom, name='deletar-sala' ),
    path('deletar-mensagem/<int:pk>/', deletarMensagem, name='deletar-mensagem'),
    path('perfil-usuario/<int:pk>/', perfilUser, name='perfil-user'),
    path('editar-usuario/', editarUsuario, name='editar-usuario'),
    path('topicos/', topicosPesquisados, name='topicos-pesquisa'),
    path('recentes/', atvsRecentes, name="recentes"),
    
    ]
