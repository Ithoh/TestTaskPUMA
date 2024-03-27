from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    office = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    start_date = models.DateField("Start Date")
    salary = models.IntegerField(default=0)

    # Self display name method
    def __str__(self):
        return self.name