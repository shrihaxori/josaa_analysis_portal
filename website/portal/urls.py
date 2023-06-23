from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("charts/", views.charts, name="charts"),
    path("predict/", views.predict, name = "predict"),
    path("contactus/", views.contact, name = "contact"),
]