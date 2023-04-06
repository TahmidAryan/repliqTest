from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    

class Device(models.Model):
    type = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    deviceId = models.CharField(max_length=100)
    conditionBefore = models.CharField(max_length=100)
    

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkOutDate = models.DateTimeField()
    returnDate = models.DateTimeField(null=True, blank=True)
    checkOutCondition = models.CharField(max_length=100)
    returnCondition = models.CharField(max_length=100, null=True, blank=True)
    