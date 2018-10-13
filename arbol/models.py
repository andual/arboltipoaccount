from django.db import models

class Account(models.Model):
	name = models.CharField(max_length=50)
	parent = models.ForeignKey('self', null = True, related_name = 'Children', 
		on_delete=  models.CASCADE)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name
	