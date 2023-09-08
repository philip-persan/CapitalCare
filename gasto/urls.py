from django.urls import path

from . import views

app_name = 'gastos'

urlpatterns = [
    path(
        'api/tipos_gastos_list/',
        views.TipoGastoAPIView.as_view(),
        name='tipo_list'
    ),
    path(
        'api/categorias_gastos_list/',
        views.CategoriaAPIView.as_view(),
        name='categoria_list'
    ),
    path(
        'api/gastos_list/',
        views.GastoAPIView.as_view(),
        name='gasto_list'
    ),
]
