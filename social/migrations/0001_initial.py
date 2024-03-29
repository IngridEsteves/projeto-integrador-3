# Generated by Django 5.0.1 on 2024-01-31 05:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
                ('nome_empresa', models.CharField(max_length=255)),
                ('imagem_perfil', models.ImageField(blank=True, null=True, upload_to='uploads/fotoperfil/')),
                ('imagem_capa', models.ImageField(blank=True, null=True, upload_to='uploads/fotocapa/')),
                ('cor', models.CharField(default='#455A64', max_length=10)),
                ('contatos', models.ManyToManyField(to='social.perfil')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to='social.perfil')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_feitos', to='social.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('data_postagem', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='uploads/postagem/')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='social.perfil')),
            ],
        ),
    ]
