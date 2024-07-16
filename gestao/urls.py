from django.urls import path

from . import views

app_name = 'gestao'

urlpatterns = [
    path('livro/<int:livro_id>', views.view, name='view'),
    path('cadastrar/', views.form, name='form'),
    path('salvar/', views.save, name='save'),
    path('', views.index, name='index'),
]
