# Ex02 Django ORM Web Application
## Date: 12.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](DJANGO.png)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from.models import Bankloan,BankAdmin
admin.site.register(Bankloan,BankAdmin)

models.py

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
  
```



## OUTPUT
![alt text](<Screenshot 2024-11-06 005014.png>)
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
