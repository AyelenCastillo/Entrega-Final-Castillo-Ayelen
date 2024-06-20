"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from MainApp.views import inicio, postres, comidas, registro, busqueda, buscar, login_view, perfil, ComidasDetail, PostresDetail,EditarComida,EditarPostre,EditarUsuario, ComidaDelete,PostreDelete,UserDelete,GestionAvatar,About
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),
    path('postres/', postres, name='postres'),
    path('comidas/', comidas, name='comidas'),
    path('registro/', registro, name='registro'),
    path('iniciosesion/', login_view, name='iniciosesion'),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name='logout'),
    path('busqueda/', busqueda, name='busqueda'),
    path('buscar/', buscar, name='buscar'),
    path('perfil/', perfil, name='perfil'),
    path('comidadetalles/<pk>', ComidasDetail.as_view(), name='comidadetalles'),
    path('postresdetalles/<pk>', PostresDetail.as_view(), name='postresdetalles'),
    path('editarcomida/<pk>', EditarComida.as_view(), name='editarcomida'),
    path('editarpostre/<pk>', EditarPostre.as_view(), name='editarpostre'),
    path('editarusuario/<pk>', EditarUsuario.as_view(), name='editarusuario'),
    path('comidadelete/<pk>', ComidaDelete.as_view(), name='comidadelete'),
    path('postresdelete/<pk>', PostreDelete.as_view(), name='postresdelete'),
    path('userdelete/<pk>', UserDelete.as_view(), name='userdelete'),
    path('avatar/', GestionAvatar, name='avatar'),
    path('about/', About, name='about'),
]
