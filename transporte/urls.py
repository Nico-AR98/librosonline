from django.urls import path
from transporte import views_correo_argentino


urlpatterns = [
    path("correo_argentino/", views_correo_argentino.correo_argentino, name="correo_argentino"),
]
