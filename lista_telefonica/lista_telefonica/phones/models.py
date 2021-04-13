from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Phone(models.Model):
	name = models.CharField(max_length=200, blank=False)
	email = models.EmailField(blank=True)
	phone_number = PhoneNumberField(blank=False)
	address = models.CharField(max_length=200, blank=True)

	#def __str__(self):
	#	return self.name

