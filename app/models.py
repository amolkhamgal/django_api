from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as needed
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    salary=models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender=models.CharField(max_length=20)
    def __str__(self):
        return self.first_name



