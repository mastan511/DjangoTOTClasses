from django.db import models

# Create your models here.
class Student(models.Model):
	rollno = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	mobileno = models.CharField(max_length=10,null = True)
	email = models.EmailField(max_length=30)
	address = models.TextField(null=True)
	def __str__(self):
		return self.name