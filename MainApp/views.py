from django.shortcuts import render, redirect
from .models import Postres, Comidas, Avatar
from .forms import EditUserForm, EditUserPasswordForm, AvatarForm, UserCreationFormWithEmail
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
from django.contrib.auth.models import User
from django.contrib import messages

def obtener_avatar_url(usuario):
    try:
        avatar = Avatar.objects.get(user=usuario)
        return avatar.imagen.url if avatar.imagen else None
    except Avatar.DoesNotExist:
        return None
    
def inicio(req):
    avatar_url = obtener_avatar_url(req.user) if req.user.is_authenticated else None
    return render(req, "inicio.html", {"avatar_url": avatar_url, "user": req.user})
    
def comidas(req):
    comidas = Comidas.objects.all()
    avatar_url = obtener_avatar_url(req.user) if req.user.is_authenticated else None

    if req.method == 'POST' and req.user.is_authenticated:
        nueva_comida = Comidas(
            titulo=req.POST['titulo'],
            receta=req.POST['receta'],
            ingredientes=req.POST['ingredientes'],
            autor=req.user
        )
        nueva_comida.save()
        return redirect('comidas')
    else:
        return render(req, "comidas.html", {"comidas": comidas, "avatar_url": avatar_url})

def postres(req):
    postres = Postres.objects.all()
    avatar_url = obtener_avatar_url(req.user) if req.user.is_authenticated else None

    if req.method == 'POST' and req.user.is_authenticated:
        nuevo_postre = Postres(
            titulo=req.POST['titulo'],
            receta=req.POST['receta'],
            ingredientes=req.POST['ingredientes'],
            autor=req.user
        )
        nuevo_postre.save()
        return redirect('postres')
    else:
        return render(req, "postres.html", {"postres": postres, "avatar_url": avatar_url})

def registro(req):
    if req.method == 'POST':
        miFormulario = UserCreationFormWithEmail(req.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            username = miFormulario.cleaned_data.get('username')
            return render(req, "inicio.html", {"message": f"Usuario {username} creado correctamente"})
        else:
            return render(req, "registro.html", {"miFormulario": miFormulario})
    else:
        miFormulario = UserCreationFormWithEmail()
        return render(req, "registro.html", {"miFormulario": miFormulario})

def busqueda(req):
    return render(req, "busqueda.html")

def buscar(req):
    titulo = req.GET.get('titulo')
    if titulo:
        resultados_postres = Postres.objects.filter(titulo__icontains=titulo)
        resultados_comidas = Comidas.objects.filter(titulo__icontains=titulo)
        resultados = list(resultados_postres) + list(resultados_comidas)
        if resultados:
            return render(req, "inicio.html", {"results": resultados})
        else:
            return render(req, "inicio.html", {"message": "No se encontraron resultados"})
    else:
        return render(req, "inicio.html", {"message": "Por favor, ingrese un término de búsqueda"})
    
def lista_postres_comidas(request):
    postres = Postres.objects.all()
    comidas = Comidas.objects.all()
    
    return render(request, 'inicio.html', {
        'postres': postres,
        'comidas': comidas,
    })

def login_view(req):
    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST)
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario=data["username"]
            psw=data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
           
                return redirect('inicio')
            else:
                mensaje = 'Usuario o contraseña incorrectos'
                return render(req, 'iniciosesion.html', {'miFormulario': miFormulario, 'mensaje': mensaje})
        else:
            mensaje = 'Formulario no válido'
            return render(req, 'iniciosesion.html', {'miFormulario': miFormulario, 'mensaje': mensaje})
    else:
        miFormulario = AuthenticationForm()

    return render(req, 'iniciosesion.html', {'miFormulario': miFormulario})
   


@login_required
def perfil(req):
    avatar_url = obtener_avatar_url(req.user)

    if req.user.is_staff:  
        comidas = Comidas.objects.all()
        postres = Postres.objects.all()
        usuarios = User.objects.all()
    else:
        comidas = Comidas.objects.filter(autor=req.user)
        postres = Postres.objects.filter(autor=req.user)
        usuarios = None
    
    return render(req, "perfil.html", {
        "user": req.user,
        "comidas": comidas,
        "postres": postres,
        "usuarios": usuarios,
        "avatar_url": avatar_url 
    })


class ComidasDetail(DetailView):
    model = Comidas
    template_name = 'comidadetalles.html'
    context_object_name = 'comida'

   
class PostresDetail(DetailView):
    model = Postres
    template_name = "postresdetalles.html"
    context_object_name = "postres"


class EditarComida(UpdateView):
    model = Comidas
    template_name = "editarcomida.html"
    fields = ('titulo', 'receta', 'ingredientes')
    success_url = reverse_lazy('perfil')
    context_object_name = 'comida'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super().form_valid(form)
    
class EditarPostre(UpdateView):
    model = Postres
    template_name = "editarpostre.html"
    fields =  ('titulo', 'receta', 'ingredientes')
    success_url = reverse_lazy('perfil')
    context_object_name = 'postres'
 
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super().form_valid(form)
    
class EditarUsuario(UpdateView):
    model = User
    template_name = "editarusuario.html"
    success_url = reverse_lazy('perfil')
    context_object_name = 'usuario'
    form_class = EditUserForm  

    def get_object(self):
        if self.request.user.is_superuser:
            return User.objects.get(pk=self.kwargs['pk'])
        else:
            return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'password_form' not in context:
            context['password_form'] = EditUserPasswordForm(user=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        password_form = EditUserPasswordForm(user=self.object, data=request.POST)

        if form.is_valid():
            return self.form_valid(form, password_form)
        else:
            return self.form_invalid(form, password_form)

    def form_valid(self, form, password_form):
        form.save()

        if password_form.is_valid():
            password_form.save()

        return redirect(self.get_success_url())

    def form_invalid(self, form, password_form):
        return self.render_to_response(
            self.get_context_data(form=form, password_form=password_form)
        )

class ComidaDelete(DeleteView):
    model = Comidas
    template_name = "comidadelete.html"
    success_url = reverse_lazy('perfil')
    context_object_name = 'comida'

class PostreDelete(DeleteView):
    model = Postres
    template_name = "postresdelete.html"
    success_url = reverse_lazy('perfil')
    context_object_name = 'postres'


class UserDelete(DeleteView):
    model = User
    template_name = "userdelete.html"
    context_object_name = 'usuario'

    def get_success_url(self):
        if self.request.user == self.get_object():
            return reverse_lazy('inicio')
        elif self.request.user.is_staff:
            return reverse_lazy('perfil')
        else:
            return reverse_lazy('perfil')



def GestionAvatar(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
        is_new_avatar = False
    except Avatar.DoesNotExist:
        avatar = None
        is_new_avatar = True

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)

        if form.is_valid():
            if 'clear' in request.POST:
                if avatar:
                    avatar.delete()
                return redirect('inicio')
            else:
                avatar_instance = form.save(commit=False)
                avatar_instance.user = request.user
                avatar_instance.save()
                return redirect('inicio')
        else:
            messages.error(request, 'Ocurrió un error al actualizar el avatar. Por favor, verifica los datos.')

    else:
        form = AvatarForm(instance=avatar)

    context = {
        'form': form,
        'is_new_avatar': is_new_avatar,
        'avatar': avatar,
    }
    return render(request, 'avatar.html', context)

def About(req):
    return render(req, 'about.html')