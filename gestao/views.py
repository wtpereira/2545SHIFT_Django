from typing import Any
from django.db.models.query import QuerySet
#from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404, render
#from django.urls import reverse, reverse_lazy
from django.urls import reverse_lazy
from django.views import generic

from .models import Livro

"""
def index(request):
    livros = Livro.objects.all()
    return render(request, 'gestao/list.html', {'livros': livros})
"""

class ListView(generic.ListView):
    template_name = 'gestao/list.html'
    context_object_name = 'livros'

    def get_queryset(self) -> QuerySet[Any]:
        return Livro.objects.all()


"""
def form(request):
    return render(request, 'gestao/form.html')
"""

"""
def save(request):
    titulo = request.POST['titulo']
    paginas = int(request.POST['paginas'])
    livro = Livro(titulo=titulo, paginas=paginas)
    livro.save()  # Comando para que o Django persista o objeto no banco de dados.
    return HttpResponseRedirect(reverse('gestao:index'))
"""

class CreateView(generic.CreateView):
    model = Livro
    template_name = 'gestao/form.html'
    success_url = reverse_lazy('gestao:index')
    fields = ['titulo', 'paginas']


"""
def view(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    # livro = Livro.objects.get(pk=livro_id)
    # livro = Livro.objects.filter(pk=livro_id).last()
    return render(request, 'gestao/view.html', {'livro': livro})
"""

class DetailView(generic.DetailView):
    model = Livro
    template_name = 'gestao/view.html'
