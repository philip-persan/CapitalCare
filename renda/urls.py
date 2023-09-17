from django.urls import path

from . import views

app_name = 'rendas'

urlpatterns = [
    path(
        'api/tipo_rendas_list/',
        views.TipoRendasAPIView.as_view(),
        name='api_list_tipos'
    ),
    path(
        'api/rendas_list/',
        views.RendasAPIView.as_view(),
        name='api_list'
    ),
    path(
        'list/',
        views.RendasListView.as_view(),
        name='rendas_list'
    ),
]
