from django.urls import path,reverse
from . import views

app_name="carro"#namespace para evitar confusiones si hay vistas similares


urlpatterns=[
    path("agregar/<int:producto_id>/",views.Agregar_producto,name="agregar"),
    path("eliminar/<int:producto_id>/",views.Eliminar_producto,name="eliminar"),
    path("restar/<int:producto_id>/",views.Restar_producto,name="restar"),
    path("limpiar/",views.Limpiar_carro,name="limpiar"),
]