from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15) 
    location = models.CharField(max_length=100)

    class Meta:
        db_table = "data"   
