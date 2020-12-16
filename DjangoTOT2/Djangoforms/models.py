from django.db import models

# Create your models here.
class Employee(models.Model):
	firstname = models.CharField(max_length=10)
	lastname = models.CharField(max_length=30)
	age = models.IntegerField()
	gender = models.CharField(max_length=10,null=True)
	branch = models.CharField(max_length=20,null=True)
	language = models.CharField(max_length=30,null=True)
	email = models.EmailField(max_length=30)
	def __str__(self):
		return self.name