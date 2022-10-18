# Generated by Django 4.0.2 on 2022-02-08 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('hash_confirm_register', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('hash_confirm_senha', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.tipousuario')),
                
            ],
        ),
    ]