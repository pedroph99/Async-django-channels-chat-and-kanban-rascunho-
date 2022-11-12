from re import template
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from .models import usuarios, Todo
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import NameForm
# Create your views here.

def home(request):
    contexto = {'titulo': 'Página de login'}
    if request.method == 'POST':
       user =  request.POST.get('usuario')
       senha = request.POST.get('senha')
       todos_usuarios = get_user_model()
       teste = authenticate(username=user, password=senha)

       if teste:
        user_logged = usuarios.objects.get(user=todos_usuarios.objects.get(username=user).pk)
        url = user_logged.get_absolute_url()
        login(request, teste)
    
        return redirect(url)

       else:
        contexto['user_logado'] = 'Usuário e senha incompatíveis'
        return render(request, 'chat_login/resultado.html',context=contexto)
    else:
        return render(request, 'chat_login/chathome.html',context=contexto)

def register(request):
    contexto = {'titulo': 'página de registro' }
    if request.method == 'POST':
        user =  request.POST.get('usuario')
        senha = request.POST.get('senha')
        info = {'usuario' : user, 'senha': senha}
        print(user)
        print(senha)
        form = NameForm(info)
        if form.is_valid():
            if form.clean_usuario():
                print('putooo')
        return render(request, 'chat_login/registro.html',context=contexto)
    else:
        return render(request, 'chat_login/registro.html',context=contexto)

class home2(UserPassesTestMixin, DetailView):
    
    model = usuarios
    context_object_name = 'usuario'
    template_name = 'chat_login/initial_page.html'

    
    def test_func(self):
        user = self.request.user.pk
        objeto_usuario = usuarios.objects.get(user=user)
        request_slug = self.request.build_absolute_uri().split('/')[-1]
       
        if objeto_usuario.slug == request_slug:
            return True


class Todo_Detail(DetailView):
    model = usuarios
    template_name = 'chat_body/todo.html'
    context_object_name = 'objeto'
    
    def get_context_data(self, **kwargs):
        print(self.query_pk_and_slug)
        contexto =  super().get_context_data(**kwargs)
        contexto['objetos_todo'] = Todo.objects.filter(user=usuarios.objects.get(pk=self.kwargs.get('pk')))
        return contexto

def muda_estado(request, pk):
    if request.method == 'POST':
        objeto = Todo.objects.get(pk=pk)
        if objeto.ativo:
            objeto.ativo = False
            print(objeto.ativo)
            objeto.save()
        else:
            objeto.ativo = True
            print(objeto.ativo)
            objeto.save()

        return render(request, 'chat_login/resultado.html')
   
    
