from django.db import models

# Create your models here.

#-----------------------------------------------------------
# Data Base Model for machine data
class MachineData_db(models.Model):
    machineCode = models.CharField(max_length= 32)
    machineText = models.CharField(max_length= 32, null= True)
    machineDescription = models.CharField(max_length= 64, null= True)
#===========================================================

#****************************************************************************************************************
#-------------------------------------------------------------------
# Sub Data Base Model for work type category 
class WorkTypes_db(models.Model):
    # Base work types data
    numberCode = models.CharField(max_length= 16)
    description = models.CharField(max_length= 64, null= True)
#===================================================================

#-------------------------------------------------------------------
# Data Base Model for work type descriprion 
class WorkData_db(models.Model):
    # Internal data
    workCode = models.CharField(max_length= 32)
    workText = models.CharField(max_length= 32, null= True)
    description = models.CharField(max_length= 64, null= True)
    # External data pointers
    workType_id = models.ForeignKey(to= WorkTypes_db, null= True, on_delete= models.SET_NULL)
#===================================================================
#****************************************************************************************************************