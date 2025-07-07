import pytest
from django.contrib.contenttypes.models import ContentType
from a10_topics.models import MachineData_db

@pytest.fixture()
def machines():
    listMachines = []
    for m in range(8):
        c = f"C{m}"
        t = f"T{m}"
        d = f"D{m}"
        listMachines.append(MachineData_db.objects.create(code=c, text=t, description=d))
    return listMachines