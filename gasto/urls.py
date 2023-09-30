from django.urls import path

from . import views

app_name = 'gastos'

urlpatterns = [
    path(
        'api/v1/tipos_de_gastos/',
        views.TipoGastoAPIView.as_view(),
        name='api_tipo_list'
    ),
    path(
        'api/v1/categorias_de_gastos/',
        views.CategoriaAPIView.as_view(),
        name='api_categoria_list'
    ),
    path(
        'api/v1/gastos/',
        views.GastoAPIView.as_view(),
        name='api_gasto_list'
    ),
    path(
        'create/',
        views.GastoCreateView.as_view(),
        name='gasto_create'
    ),
    path(
        'list/',
        views.GastoListView.as_view(),
        name='gasto_list'
    )
]
