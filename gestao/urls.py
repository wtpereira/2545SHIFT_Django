from django.urls import path

from . import views

app_name = 'gestao'

urlpatterns = [
    path('livro/<int:pk>', views.DetailView.as_view(), name='view'),  # path('livro/<int:livro_id>', views.view, name='view'),
    # path('cadastrar/', views.form, name='form'),
    path('salvar/', views.CreateView.as_view(), name='save'),  # path('salvar/', views.save, name='save'),
    path('', views.ListView.as_view(), name='index'),  # path('', views.index, name='index'),
]
