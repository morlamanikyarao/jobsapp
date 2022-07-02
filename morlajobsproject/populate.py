import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','morlajobsproject.settings')
import django
django.setup()
from testapp.models import hydjobs ,banglorejobs,punejobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
     d1=randint(6,9)
     num=str(d1)
     for i in range(9):
          num=num+str(randint(0,9))
     return int(num)

def populate(n):
     for i in range(n):
          fdate = fake.date()
          fcompany = fake.company()
          frole=fake.random_element(elements = ('product manager','Team Lead','Software Engineer','associate Engineer'))
          felgibility=fake.random_element(elements = ('B.TECH','M.TECH','MCA','ANY COMUTERS DEGREE'))
          faddress = fake.address()
          femail = fake.email()
          fphonenumber=phonenumbergen()
          fsalary = fake.random_element(elements=('500000','1000000','2500000','360000'))
          hyd_jobs_record = hydjobs.objects.get_or_create(date=fdate,company=fcompany,role=frole,elgibility=felgibility,address=faddress,email=femail,phonenumber=fphonenumber,salary=fsalary)


n=int(input('enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully')
