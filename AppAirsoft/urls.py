from django.urls import path, include
from AppAirsoft.views import *

urlpatterns = [
    path("", vista_inicio, name = "AppAirsoft-inicio"), 
    path("registro/", vista_registro, name = "AppAirsoft-registro"),
    path("equipamiento/", vista_equipamiento, name = "AppAirsoft-equipamiento"),
    path("replica/", vista_replica, name="AppAirsoft-replica"),
    path("iniciar_sesion/", vista_inicio_sesion, name="AppAirsoft-iniciar-sesion"),
    path("busqueda/", vista_busqueda, name="AppAirsoft-busqueda"),
 

]