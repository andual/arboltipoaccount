from django.db import models

class Account(models.Model):
	name = models.CharField(max_length=50)
	Type = models.CharField(max_length=50, default='')
	parent = models.ManyToManyField('self', related_name = 'Children',)
	number = models.IntegerField(default=0)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name
	