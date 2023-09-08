
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('rendas/', include('renda.urls')),
    path('investimentos/', include('investimento.urls')),
    path('gastos/', include('gasto.urls')),
    path('admin/', admin.site.urls),
]
