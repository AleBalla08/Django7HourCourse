from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topico, Mensagem
from .forms import RoomForm, TopicoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# rooms = [
#     {'id':1, 'nome':'alexandre'},
#     {'id':2, 'nome':'pedro'},
#     {'id':3, 'nome':'paulo'},
# ]

def loginPag(request):
    pagina = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        try:
            usuario = User.objects.get(username=username)
        except: 
            messages.error(request, 'Usuário não encontrado!')
    
        usuario = authenticate(request, username=username, password=senha)
        if usuario is not None:
            login(request, usuario)
            #messages.success(request, 'login realizado com sucesso, seja bem vindo!')
            return redirect('home')
        else:
            messages.error(request, 'Usuario ou Senha não existem')
        
            

    context = {'pagina':pagina}
    return render(request, 'principal/login-registro.html', context)


def logoutUsuario(request):
    logout(request)
    return redirect('home')

def registrarUsuario(request):
    registro = UserCreationForm()
    if request.method == 'POST':
        registro = UserCreationForm(request.POST)
        if registro.is_valid:
            usuario = registro.save(commit=False)
            usuario.username = usuario.username.lower()
            usuario.save()
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'Algo deu errado, verifique suas credenciais')



    context = {'registro':registro}
    return render(request, 'principal/login-registro.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topico__nome__icontains=q) |
        Q(nome__icontains=q) |
        Q(descricao__icontains=q)                    
                                 ).order_by('-criada')
    
    
    topicos = Topico.objects.all()
    mensagens_sala = Mensagem.objects.filter(room__topico__nome__icontains=q).order_by('-enviada')
    room_count = rooms.count()
   

    context = {'rooms': rooms, 'topicos':topicos, 'room_count':room_count, 'mensagens':mensagens_sala}
    return render(request, 'principal/index.html', context)

def room(request, pk):
    room = Room.objects.order_by('-criada').get(id=pk)
    participantes = room.participantes.all()
    
    # Fetch messages ordered by 'enviada' from the room
    mensagens_sala = room.mensagem_set.all().order_by('-enviada')
    
    if request.method == 'POST':
        mensagem = Mensagem.objects.create(
            user=request.user,
            room=room, 
            texto=request.POST.get('texto')
        )
        room.participantes.add(request.user)
        return redirect('room', pk=room.id)
    
    #print(f'Room ID: {room.id}, Participants: {participantes.count()}')
    #print(f'Messages Count: {mensagens_sala.count()}')
    #for mensagem in mensagens_sala:
        #print(f'Mensagem: {mensagem.texto}, Enviada: {mensagem.enviada}')

    context = {
        'room': room,
        'mensagens': mensagens_sala,
        'participantes': participantes
    }
    return render(request, 'principal/room.html', context)


def deletarMensagem(request, pk):
    mensagem = Mensagem.objects.get(id=pk)
    if request.method == 'POST':
        mensagem.delete()
        return redirect('home')
        
    return render(request, 'principal/deletar.html', {'obj':mensagem} )

@login_required(login_url='pagina-login')
def criarRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            room = form.save(commit=False)
            room.adm = request.user
            room.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'principal/criar-sala.html', context)


@login_required(login_url='pagina-login')
def editarRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context={'form':form}

    return render(request, 'principal/criar-sala.html', context)

@login_required(login_url='pagina-login')
def deletarRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'principal/deletar.html', {'obj':room} )    


def perfilUser(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    topicos = Topico.objects.all()
    mensagens = user.mensagem_set.all()
    context = {'user':user, 'rooms':rooms, 'topicos':topicos, 'mensagens':mensagens}
    return render(request, 'principal/perfil.html', context)

def criarTopico(request):
    form = TopicoForm(request.POST) 
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'principal/novo_topico.html', context )
