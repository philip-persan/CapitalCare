from django.urls import path

from . import views

app_name = 'investimentos'

urlpatterns = [
    path(
        'api/tipo_investimentos_list/',
        views.TipoInvestimentosAPIView.as_view(),
        name='api_tipo_invest'
    ),
    path(
        'api/investimentos_list/',
        views.InvestimentosAPIView.as_view(),
        name='api_investimentos'
    ),
]
