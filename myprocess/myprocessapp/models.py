from django.db import models

class ProcessParameterSample(models.Model):
    date = models.DateField()
    time = models.TimeField()
    output = models.BooleanField()
    value_02 = models.IntegerField()
    start = models.BooleanField()
    stop = models.BooleanField()
    value_01 = models.IntegerField()

class ProcessParameter(models.Model):
    date = models.DateField()
    time = models.TimeField()
    shift = models.SmallIntegerField()
    lot_number = models.BigIntegerField()
    batch_number = models.BigIntegerField()
    pp1 = models.DecimalField(max_digits=10, decimal_places=4)
    pp2 = models.DecimalField(max_digits=10, decimal_places=4)
    pp3 = models.DecimalField(max_digits=10, decimal_places=4)
    pp4 = models.DecimalField(max_digits=10, decimal_places=4)
    pp5 = models.DecimalField(max_digits=10, decimal_places=4)
    pp6 = models.DecimalField(max_digits=10, decimal_places=4)
    pp7 = models.DecimalField(max_digits=10, decimal_places=4)
    name = models.CharField(max_length=25)
