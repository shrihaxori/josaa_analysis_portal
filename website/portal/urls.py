from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("charts/", views.charts, name="charts"),
    path("predict/", views.contact, name = "contact"),
    path("contact/", views.predict, name = "predict"),
]