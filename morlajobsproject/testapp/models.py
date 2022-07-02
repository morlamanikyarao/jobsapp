from django.db import models

# Create your models here.
class hydjobs(models.Model):
     date=models.DateField()
     company=models.CharField(max_length=100)
     role=models.CharField(max_length=100)
     elgibility=models.CharField(max_length=100)
     address=models.CharField(max_length=100)
     email=models.EmailField()
     phonenumber=models.BigIntegerField()
     salary=models.FloatField()

class banglorejobs(models.Model):
     date=models.DateField()
     company=models.CharField(max_length=100)
     role=models.CharField(max_length=100)
     elgibility=models.CharField(max_length=100)
     address=models.CharField(max_length=100)
     email=models.EmailField()
     phonenumber=models.BigIntegerField()
     salary=models.FloatField()

class punejobs(models.Model):
     date=models.DateField()
     company=models.CharField(max_length=100)
     role=models.CharField(max_length=100)
     elgibility=models.CharField(max_length=100)
     address=models.CharField(max_length=100)
     email=models.EmailField()
     phonenumber=models.BigIntegerField()
     salary=models.FloatField()
