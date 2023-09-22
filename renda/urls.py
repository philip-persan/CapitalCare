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
    path(
        'create/',
        views.RendasCreateView.as_view(),
        name='rendas_create'
    ),
    path(
        'delete/<int:id>/',
        views.RendasDeleteView.as_view(),
        name='rendas_delete'
    ),
    path(
        'update/<int:id>/',
        views.RendasUpdateView.as_view(),
        name='rendas_update'
    ),
]
