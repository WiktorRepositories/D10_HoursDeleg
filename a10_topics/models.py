from django.db import models

# Create your models here.

#-----------------------------------------------------------
# Data Base Model for machine data
class MachineData_db(models.Model):
    code = models.CharField(max_length= 32)
    text = models.CharField(max_length= 32, null= True)
    description = models.CharField(max_length= 64, null= True)
#===========================================================

#****************************************************************************************************************
#-------------------------------------------------------------------
# Sub Data Base Model for work type category 
class WorkTypes_db(models.Model):
    # Base work types data
    code = models.CharField(max_length= 16)
    description = models.CharField(max_length= 64, null= True)
#===================================================================

#-------------------------------------------------------------------
# Data Base Model for work type descriprion 
class WorkData_db(models.Model):
    # Internal data
    code = models.CharField(max_length= 32)
    text = models.CharField(max_length= 32, null= True)
    description = models.CharField(max_length= 64, null= True)
    # External data pointers
    workType_id = models.ForeignKey(to= WorkTypes_db, null= True, on_delete= models.SET_NULL)
#===================================================================
#****************************************************************************************************************