"""biolimpieza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from biolimpieza import views

urlpatterns = [
    path('administracion/', admin.site.urls),
    path('admindashboard/', views.mostrar_sitio_administrativo),
    path('', views.mostrar_inicio, name="mostrar_inicio"),
    path('i2/', views.mostrar_inicio_2, name="mostrar_inicio_2"),
    path('ingreso/', views.mostrar_ingreso, name="ingreso"),
    path('registro/', views.mostrar_registro, name="registro"),
    path('recuperaciondeacceso/', views.mostrar_recuperacion_acceso, name="recuperacion_acceso"),
    path('restablecimientodecontrasena/<str:uidb64>/<str:token>/', views.mostrar_restablecimiento_pase, name='restablecimiento_pase'),
    path('gestionarmisdatos/', views.mostrar_gestion_datos, name="gestion_datos"),
    path('gestionarmispedidos/', views.mostrar_gestion_pedidos, name="gestion_pedidos"),
    path('gestionarmisdatos/eliminarcuenta/', views.mostrar_eliminar_cuenta, name="elimnar_cuenta"),
    path('contacto/', views.mostrar_contacto, name="contacto"),
    path('cerrarsesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('colaboradoras/', views.mostrar_colaboradoras),
    path('reserva/limpieza/<servicio>', views.mostrar_datos_reserva),
    path('agenda/<int:cod_serv>/<int:cod_pedido>/<int:cod_receptor>', views.mostrar_agenda, name="mostrar_agenda"),
    path('adminagenda/', views.mostrar_agenda_admin, name="mostrar_agenda_adm"),
    path('adminagenda/asignar/', views.asignar_agenda_admin, name="asignar_agenda_adm"),
    path('politicadetratamientodedatos/', views.mostrar_politica_tratamiento_datos),
    path('terminosycondiciones/', views.mostrar_terminos_condiciones),
    path('brigada/cotizacion/', views.mostrar_cotizacion_brigada, name="cotizar_brigada"),
    path('pasareladepago/<int:cod_factura>', views.mostrar_pasarela_pago, name="mostar_pasarela_pagos"),
    path('pasareladepago/paypal/', views.mostrar_pasarela_pay_pal),
    path('pasareladepago/transaccion/', views.crear_transaccion, name="crear_transaccion"),
    path('conocenos/', views.mostrar_conocenos, name="conocenos"),
    path('autorizacion/<int:id_factura>', views.actualizar_estado_prestac_serv, name="token_pago"),
    path('<valor>/', views.mostrar_no_encontrada, name="pag_no_econtrada")
]
