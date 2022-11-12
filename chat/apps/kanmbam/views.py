from django.shortcuts import render
from .models import tarefa
# Create your views here.
def kanmbam_home(request):
    if request.method == 'POST':
        total = len(tarefa.objects.filter(tipo='AF')) + len(tarefa.objects.filter(tipo='FE'))
        for x in range(1, total+1):
            value = request.POST.get('input%s' %x)
            print('----------------------------------------------')
            print(value + ' ' + 'This is the value')
            Tarefa = tarefa.objects.get(id=x)
            print(Tarefa.nome + 'Valor da tarefa')
            print(Tarefa.tipo + 'Valor do banco de dados antes')
            print('------------------------------------------------')
            Tarefa.tipo = value
            Tarefa.save()

        contexto = {}
        contexto['afazer'] = tarefa.objects.filter(tipo='AF')
        contexto['feito'] = tarefa.objects.filter(tipo='FE')
        return render(request, 'kanmbam/sortable.html', contexto)

    else:
        contexto = {}
        contexto['afazer'] = tarefa.objects.filter(tipo='AF')
        contexto['feito'] = tarefa.objects.filter(tipo='FE')
        print(contexto['afazer'])
        return render(request, 'kanmbam/sortable.html', contexto)
