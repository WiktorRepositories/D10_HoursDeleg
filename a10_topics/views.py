from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from a10_topics.models import MachineData_db, WorkTypes_db, WorkData_db

# Create your views here.
class View_machines_overview(View):
    URL_NAME = "machines_overview"
    HTML_NAME = "machines_overview.html"
    # Method get 'default'
    def get(self, request:HttpRequest):
        all_machines = MachineData_db.objects.all()
        context = {"machines" : all_machines}
        return render(request= request, template_name= View_machines_overview.HTML_NAME, context= context)

    # Method post, form is send
    def post(self, request:HttpRequest):
        code = request.POST.get("code", "")
        text = request.POST.get("text", "")
        desc = request.POST.get("desc", "")
        if code and text and desc:
            MachineData_db.objects.create(machineCode=code, machineText= text, machineDescription= desc)
        else:
            pass # redirect to error info page...
        return HttpResponseRedirect(reverse(View_machines_overview.URL_NAME))


class View_machines_search(View):
    # Method get 'default'
    def get(self, request:HttpRequest):
        pass

    # Method post, form is send
    def post(self, request:HttpRequest):
        pass

class View_machine_modify(View):
    # Method get 'default'
    def get(self, request:HttpRequest, id):
        machine = MachineData_db.objects.get(pk=id)
        context = {"machine" : machine}
        return render(request= request, template_name= "machine_modify.html", context= context)

    # Method post, form is send
    def post(self, request:HttpRequest, id):
        code = request.POST.get("code", "")
        text = request.POST.get("text", "")
        desc = request.POST.get("desc", "")
        if code and text and desc:
            machine = MachineData_db.objects.get(pk=id)
            machine.machineCode = code
            machine.machineText = text
            machine.machineDescription = desc
            machine.save()
        else:
            pass # redirect to error info page...
        return HttpResponseRedirect(reverse(View_machines_overview.URL_NAME))

class View_machine_delete(View):
    # Method get 'default'
    def get(self, request:HttpRequest, id):
        machine = MachineData_db.objects.get(pk=id)
        context = {"machine" : machine}
        return render(request= request, template_name="machine_delete.html", context= context)

    # Method post, form is send
    def post(self, request:HttpRequest, id):
        if request.POST.get("operation", "") == "delete":
            machine = MachineData_db.objects.get(pk= id)
            machine.delete()
        return HttpResponseRedirect(reverse(View_machines_overview.URL_NAME))

