# Ex02 Django ORM Web Application
## Date: 29.09.25

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).





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
from . models import car


# Register your models here.
admin.site.register(car)

class CarAdmin(admin.ModelAdmin):
    list_display=('car_id','brand','model','year','price')

models.py

from django.db import models



class car(models.Model):

    car_id = models.AutoField(primary_key=True)

    brand = models.CharField(max_length=20)

    model = models.CharField(max_length=20)

    year = models.DateField()

    price = models.IntegerField()

```



## OUTPUT
![alt text](<Screenshot 2025-09-29 093637.png>)

![alt text](<Screenshot 2025-09-29 120132.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
