# Generated by Django 3.2.25 on 2024-10-15 18:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0003_auto_20241015_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participantes',
            field=models.ManyToManyField(blank=True, related_name='participantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
