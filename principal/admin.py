from django.contrib import admin
from .models import Room, Topico, Mensagem
# Register your models here.
admin.site.register(Room)
admin.site.register(Mensagem)
admin.site.register(Topico)