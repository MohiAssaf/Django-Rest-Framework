from django.db import models

class Company(models.Model):
    NAME_MAX = 20
    DESC_MAX = 300
    
    
    name = models.CharField(
        max_length=NAME_MAX,     
    )
    
    logo = models.ImageField(
        upload_to='logos/',
        null=True,
        blank=True
        )
    
    description = models.TextField(
        max_length=DESC_MAX
    )
    
    



class Employee(models.Model):
    NAMES_MAX = 15
    
    POS_MAX = 10
    
    MAX_DIGITS = 8
    DECI_PLACE = 2
    
    
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    
    first_name = models.CharField(
        max_length=NAMES_MAX,

    )
    
    last_name = models.CharField(
        max_length=NAMES_MAX,

    )
    
    date_of_birth = models.DateField()
    
    photo = models.ImageField(
        upload_to='photos/',
        null=True,
        blank=True,
    )
    
    position = models.CharField(
        max_length=POS_MAX
    )
    
    
    salary = models.DecimalField(
        max_digits=MAX_DIGITS, 
        decimal_places=DECI_PLACE
    )
    