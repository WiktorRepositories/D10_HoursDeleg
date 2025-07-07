from django.urls import path
from djangoproject import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", view= views.main_page, name="home"),
    path("", TemplateView.as_view(template_name="main_page.html"), name="home"),
]