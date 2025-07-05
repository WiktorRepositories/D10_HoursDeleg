from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from a10_topics.models import MachineData_db, WorkTypes_db, WorkData_db

# Create your views here.
class View_machine_overview(View):
    # Method get 'default'
    def get(self, request:HttpRequest):
        pass

    # Method post, form is send
    def post(self, request:HttpRequest):
        pass


class View_machine_delete(View):
    # Method get 'default'
    def get(self, request:HttpRequest):
        pass

    # Method post, form is send
    def post(self, request:HttpRequest):
        pass

class View_machine_modify(View):
    # Method get 'default'
    def get(self, request:HttpRequest):
        pass

    # Method post, form is send
    def post(self, request:HttpRequest):
        pass