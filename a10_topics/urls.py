from django.urls import path
from a10_topics import views

urlpatterns = [
    # URLS for machine data menagment
    path(route= "machines_overview/", view= views.View_machines_overview.as_view(), name= "machines_overview"),
    path(route= "machines_search/", view= views.View_machines_search.as_view(), name= "machines_search"),
    path(route= "machine_delete/<int:id>", view= views.View_machine_delete.as_view(), name= "machine_delete"),
    path(route= "machine_modify/<int:id>", view= views.View_machine_modify.as_view(), name= "machine_modify"),

    # URLS for work types data menagment

    # URLS for work data data menagment
]