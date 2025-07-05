from django.urls import path
from a10_topics import views

urlpatterns = [
    # URLS for machine data menagment
    path(route= "machine_overview/", view= views.View_machine_overview.as_view(), name= "machine_overview"),
    path(route= "machine_delete/<int:pk>", view= views.View_machine_delete.as_view(), name= "machine_delete"),
    path(route= "machine_modify/<int:pk>", view= views.View_machine_modify.as_view(), name= "machine_modify"),

    # URLS for work types data menagment

    # URLS for work data data menagment
]