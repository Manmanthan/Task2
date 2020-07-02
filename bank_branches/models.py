from django.db import models


# Create your models here.

class Banks(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=49)

    def __str__(self):
        return self.name


class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11, null=False)
    bank_id = models.ForeignKey(Banks, on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    def __str__(self):
        return self.ifsc