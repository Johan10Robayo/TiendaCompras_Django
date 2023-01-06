from django.urls import path
from .views import Vregistro
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', Vregistro.as_view, name='Autenticacion'),
    ]