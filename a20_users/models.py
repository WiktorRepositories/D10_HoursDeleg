from django.db import models
from django.contrib.auth.models import User
from a10_topics.models import MachineData_db, WorkData_db, WorkTypes_db

# Create your models here.

#-----------------------------------------------------------------------------------------------------------
# class UserDataInstance_t(models.Model):
#     # Prototype of new instance template for new user
#     daydate = models.DateField(auto_now= False, auto_now_add= False, unique= False)

#     travelstart = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)
#     travelend = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)

#     workstart = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)
#     workend = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)

#     fk_machine_pk = models.ForeignKey(to= MachineData_db, null= True)
#     fk_work_pk = models.ForeignKey(to= WorkData_db, null= True)
#===========================================================================================================

#-----------------------------------------------------------------------------------------------------------
class UserData_db(models.Model):
    # User primary key taken from current logged user.
    user_id = models.IntegerField()

    daydate = models.DateField(auto_now= False, auto_now_add= False, unique= False)

    travelstart = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)
    travelend = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)

    workstart = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)
    workend = models.TimeField(auto_now= False, auto_now_add= False, unique= False, null= True)

    fk_machine_pk = models.ForeignKey(to= MachineData_db, null= True, on_delete= models.SET_NULL)
    fk_work_pk = models.ForeignKey(to= WorkData_db, null= True, on_delete= models.SET_NULL)
    fk_code_pk = models.ForeignKey(to= WorkTypes_db, null= True, on_delete= models.SET_NULL)
#===========================================================================================================