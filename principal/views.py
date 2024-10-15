from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topico
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# rooms = [
#     {'id':1, 'nome':'alexandre'},
#     {'id':2, 'nome':'pedro'},
#     {'id':3, 'nome':'paulo'},
# ]

def loginPag(request):
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
            return redirect('home')
        else:
            messages.error(request, 'Usuario ou Senha não existem')
        
            

    context = {}
    return render(request, 'principal/pagina-login.html', context)


def logoutUsuario(request):
    logout(request)
    return redirect('home')



def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topico__nome__icontains=q) |
        Q(nome__icontains=q) |
        Q(descricao__icontains=q)                    
                                 )
    
    
    topicos = Topico.objects.all()

    room_count = rooms.count()
   

    context = {'rooms': rooms, 'topicos':topicos, 'room_count':room_count}
    return render(request, 'principal/index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'room':room}
    return render(request, 'principal/room.html', context)

@login_required(login_url='pagina-login')
def criarRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
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
