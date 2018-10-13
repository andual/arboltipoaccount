from django.db import models
from pygments import highlight

class Account(models.Model):
	number = models.AutoField(primary_key=True, default=0)
	name = models.CharField(max_length=50)
	Type = models.CharField(max_length=50, null=True)
	parent = models.ManyToManyField('self', related_name = 'Children',)
	owner = models.ForeignKey('auth.User', related_name='Account', on_delete=models.CASCADE)
	highlighted = models.TextField()
	class Meta:
		ordering = ('name',)

	def save(self, *args, **kwargs):
		self.highlighted = highlight(self.name, self.Type, self.parent)
		super(Account, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
	