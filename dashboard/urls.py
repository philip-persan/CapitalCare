from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('visao_geral/', views.VisaoGeralView.as_view(), name='visao_geral'),
]
