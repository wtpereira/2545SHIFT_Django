from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Livro


def index(request):
    livros = Livro.objects.all()
    return render(request, 'gestao/list.html', {'livros': livros})

def form(request):
    return render(request, 'gestao/form.html')

def save(request):
    titulo = request.POST['titulo']
    paginas = int(request.POST['paginas'])
    livro = Livro(titulo=titulo, paginas=paginas)
    livro.save()  # Comando para que o Django persista o objeto no banco de dados.
    return HttpResponseRedirect(reverse('gestao:index'))

def view(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'gestao/view.html', {'livro': livro})
