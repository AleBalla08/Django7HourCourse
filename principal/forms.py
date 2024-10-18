from django.forms import ModelForm
from .models import Room, Topico
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['adm', 'participantes']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

