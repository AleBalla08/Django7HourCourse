from django.urls import path
from .views import home, room, criarRoom, editarRoom, deletarRoom, loginPag, logoutUsuario

urlpatterns = [
    path('login/', loginPag, name='pagina-login'),
    path('logout/', logoutUsuario, name='pagina-logout'),
    path('', home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('criar-sala/', criarRoom, name='criar-sala' ),
    path('editar-sala/<int:pk>/', editarRoom, name='editar-sala' ),
    path('deletar-sala/<int:pk>/', deletarRoom, name='deletar-sala' ),
]
