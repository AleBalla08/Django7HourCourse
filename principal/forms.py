from django.forms import ModelForm
from .models import Room, Topico

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['adm', 'participantes']


class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = '__all__'

