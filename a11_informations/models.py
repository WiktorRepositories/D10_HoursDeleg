from django.db import models
from time import time

# Create your models here.

#--------------------------------------------------------------------------------------------------------------------
# Data Base for constant waork and break time
class WorkTime_db(models.Model):
    # Base data types
    srccode = models.CharField(max_length= 8, null= False)
    description = models.CharField(max_length= 16, null= True)
    workTime = models.TimeField(auto_now= False, auto_now_add= False)
    breakTime = models.TimeField(auto_now= False, auto_now_add= False)

    # Django admin display
    def __str__(self):
        return f"Work: {self.workTime}, Break:{self.breakTime}"
#====================================================================================================================

#--------------------------------------------------------------------------------------------------------------------
class MailReciever_db(models.Model):
    # Base data types
    srccode = models.CharField(max_length= 8, unique= False)
    email = models.CharField(max_length= 32) 

    firstName = models.CharField(max_length= 16)
    lastName = models.CharField(max_length= 16)
    description = models.CharField(max_length= 32, null= True) 

    # Django admin display
    def __str__(self):
        return f"mail: {self.email}, {self.firstName} {self.lastName}"
#====================================================================================================================