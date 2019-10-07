from django.db import models


class Machine(models.Model):
    machine_id = models.CharField(max_length=30)
    machine_number = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
