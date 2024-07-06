from django.db import models

# Create your models here.
class Cust(models.Model):
    username=models.CharField(max_length=244)
    password=models.CharField(max_length=244)
    def __str__(self):
        return f"{self.username}"
class Task(models.Model):
    username=models.CharField(max_length=244)
    title=models.CharField(max_length=244)
    description=models.CharField(max_length=244)
    status=models.CharField(max_length=244)
    duedate=models.DateField()
    def __str__(self):
        return f"{self.username}"