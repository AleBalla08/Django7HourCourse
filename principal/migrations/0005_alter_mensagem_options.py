# Generated by Django 3.2.25 on 2024-10-15 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_room_participantes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensagem',
            options={'ordering': ['-enviada']},
        ),
    ]
