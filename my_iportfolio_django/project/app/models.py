from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Members(models.Model):
    i_name = models.CharField(max_length=40,default='empyty')
    i_email = models.CharField(max_length=40,default='empyty')
    i_subject = models.CharField(max_length=40,default='empyty')
    i_message = models.CharField(max_length=40,default='empyty')
    def __str__(self):
        return self.i_name