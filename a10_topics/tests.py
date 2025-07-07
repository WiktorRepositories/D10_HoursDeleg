import pytest
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from a10_topics.models import MachineData_db

#-------------------------------------------------------------------------

@pytest.mark.django_db
def test_machine_overview_get(machines):
    client = Client()
    url = reverse("machines_overview")
    response = client.get(url)

    assert response.status_code == 200
    assert response.context["machines"].count() == len(machines)
    for m in machines:
        assert m in response.context["machines"]

@pytest.mark.django_db
def test_machine_overview_post(machines):
    client = Client()
    url = reverse("machines_overview")
    data = {"code" : "C00", "text" : "T00", "description" : "D00"}
    response = client.post(path= url, data=data)

    assert response.status_code == 302
    assert MachineData_db.objects.get(**data)

#-------------------------------------------------------------------------

@pytest.mark.parametrize("idx", [0,1,2,3,4,5,6,7])
@pytest.mark.django_db
def test_machine_modify_get(machines, idx):
    pk = machines[idx].pk
    client = Client()
    url = reverse(viewname= "machine_modify", args=[pk])
    response = client.get(path= url)
    assert response.status_code == 200

@pytest.mark.parametrize("idx", [0,1,2,3,4,5,6,7])
@pytest.mark.django_db
def test_machine_modify_post(machines, idx):
    pk = machines[idx].pk
    client = Client()
    url = reverse(viewname= "machine_modify", args=[pk])
    data = {"code" : "C11", "text" : "T11", "description" : "D11"}
    response = client.post(url, data)

    assert response.status_code == 302
    assert MachineData_db.objects.get(**data)

#-------------------------------------------------------------------------

@pytest.mark.parametrize("idx", [0,1,2,3,4,5,6,7])
@pytest.mark.django_db
def test_machine_delete_get(machines, idx):
    client = Client()
    url = reverse(viewname= "machine_delete", args=[machines[idx].pk])
    response = client.get(path= url)
    assert response.status_code == 200

@pytest.mark.parametrize("idx", [0,1,2,3,4,5,6,7])
@pytest.mark.django_db
def test_machine_delete_post(machines, idx):
    pk = machines[idx].pk
    client = Client()
    data = {"operation" : "delete"}
    url = reverse(viewname= "machine_delete", args=[pk])
    response = client.post(path= url, data= data)

    assert response.status_code == 302
    try:
        MachineData_db.objects.get(pk=pk)
        assert False
    except MachineData_db.DoesNotExist:
        assert True

#-------------------------------------------------------------------------