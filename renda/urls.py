from django.urls import path

from . import views

app_name = 'rendas'

urlpatterns = [
    path(
        'api/v1/tipos_de_rendas/',
        views.TipoRendasAPIView.as_view(),
        name='api_list_tipos'
    ),
    path(
        'api/v1/rendas/',
        views.RendasAPIView.as_view(),
        name='api_list'
    ),
    path(
        'api/v1/agreggations/',
        views.RendasAgreggationsAPIView.as_view(),
        name='api_agreggations'
    ),
    path(
        'api/v1/annotations/',
        views.RendasAnnotationsAPIView.as_view(),
        name='api_annotations'
    ),
    path(
        'create/',
        views.RendasCreateView.as_view(),
        name='rendas_create'
    ),
    path(
        'list/',
        views.RendasListView.as_view(),
        name='rendas_list'
    ),
    path(
        'update/<int:id>/',
        views.RendasUpdateView.as_view(),
        name='rendas_update'
    ),
    path(
        'delete/<int:id>/',
        views.RendasDeleteView.as_view(),
        name='rendas_delete'
    ),
    path(
        'delete/tipo/<int:id>/',
        views.TipoRendasDeleteView.as_view(),
        name='tipo_rendas_delete'
    ),
]
