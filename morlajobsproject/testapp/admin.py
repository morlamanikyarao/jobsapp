from django.contrib import admin
from testapp.models import hydjobs,banglorejobs,punejobs

# Register your models here.
class hydjobsadmin(admin.ModelAdmin):
     list_display=['date','company','role','elgibility','address','email','phonenumber','salary']

admin.site.register(hydjobs,hydjobsadmin)


class banglorejobsadmin(admin.ModelAdmin):
     list_display=['date','company','role','elgibility','address','email','phonenumber','salary']

admin.site.register(banglorejobs,banglorejobsadmin)


class punejobsadmin(admin.ModelAdmin):
     list_display=['date','company','role','elgibility','address','email','phonenumber','salary']

admin.site.register(punejobs,punejobsadmin)
