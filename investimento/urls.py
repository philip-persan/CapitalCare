from django.urls import path

from . import views

app_name = 'investimentos'

urlpatterns = [
    path(
        'api/v1/tipos_de_investimentos/',
        views.TipoInvestimentosAPIView.as_view(),
        name='api_tipo_invest'
    ),
    path(
        'api/v1/investimentos/',
        views.InvestimentosAPIView.as_view(),
        name='api_investimentos'
    ),
    path(
        'create/',
        views.InvestimentoCreateView.as_view(),
        name='investimentos_create'
    ),
    path(
        'list/',
        views.InvestimentosListView.as_view(),
        name='investimentos_list'
    ),
    path(
        'update/<int:id>/',
        views.InvestimentoUpdateView.as_view(),
        name='investimentos_update'
    ),
    path(
        'delete/<int:id>/',
        views.InvestimentoDeleteView.as_view(),
        name='investimentos_delete'
    ),
    path(
        'tipo/create/',
        views.TipoInvestimentoCreateView.as_view(),
        name='tipo_create'
    ),
    path(
        'tipo/delete/<int:id>/',
        views.TipoInvestimentoDeleteView.as_view(),
        name='tipo_delete'
    )
]
