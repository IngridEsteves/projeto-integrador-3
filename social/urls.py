from django.urls import path
from social import views
from usuarios import views as view_usuario

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='social'),#ok
    path('perfil/<int:perfil_id>/', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar/',views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer/',views.desfazer_amizade, name='desfazer'),
    path('perfil/<int:convite_id>/aceitar/',views.aceitar, name='aceitar'),
    path('perfil/<int:convite_id>/rejeitar/',views.rejeitar, name='rejeitar'),
    path('encontrar/', views.buscar_usuario, name='buscar_usuario'),
    path('conexoes/', views.conexoes, name='conexoes'),
    path('alterarperfil/', views.alterar_perfil, name='alterar_perfil'),
    path('alterarcapa/', views.alterar_capa, name='alterar_capa'),
    path('alterarcor/', views.alterar_cor, name='alterar_cor'),


    #Perfil Postagem, Funcoes de postagem estão todas ok!
    path('postagem/', views.postagem, name='postagem'),
    path('deletepostagem/<int:id_postagem>', views.delete_postagem, name='delete_postagem'),
    path('minhaspostagem/', views.minhas_postagens, name='minhas_postagens'),
    path('excluirpostagem/<int:id_postagem>', views.excluir_postagem, name='excluir_postagem'),
]

# Função para que o django mostre imagens durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)