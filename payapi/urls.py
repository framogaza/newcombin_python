"""payapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from payapi import views
from payapi import TransactionsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    ####CONSULTAR LISTADO DE BOLETAS
    ##path('boletas/',views.boleta_listado),
    
    path('boleta/',views.boleta_nueva),

    ####CONSULTAR INFORMACION DE BOLETA ESPECIFICA
    ##path('boletas/<int:codigoBarra>',views.boleta_detalle),

    path('boletas/impagas/<str:tipoServicio>',views.boletas_impagas_filtro),
    path('boletas/impagas/',views.boletas_impagas),
    
    path('transaction/',TransactionsViews.new_transaction),
    path(r'^transactions/(?P<dateFrom>[\w\-\.]+)/(?P<dateTo>[\w\-\.]+)/$',TransactionsViews.list_transaction),
    
    ####CONSULTA DE LISTADO DE TRANSACCIONES
    ##path('transactions/',TransactionsViews.list_transaction)
]
