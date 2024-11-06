from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
    bid=models.CharField(max_length=20,primary_key="bid")
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    interst=models.IntegerField()
    email=models.EmailField()
class BankAdmin(admin.ModelAdmin):
  list_display=('bid','name','amount','interst','email')




# Create your models here.
