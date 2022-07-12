from django import views
from django.urls import path
from . import views





urlpatterns = [

    path('pacientes/', views.pacientes, name="pacientes"),
    path('dados_paciente/', views.dados_paciente_listar, name="dados_paciente_listar"),
    path('dados_pacientes/<str:id>/', views.dados_paciente, name="dados_paciente")


]