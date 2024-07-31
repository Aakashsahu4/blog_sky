from django.db import models


class Logo(models.Model):

	title = models.CharField(max_length=20)
	file = models.ImageField(upload_to='logos')

	def __str__(self):
		return self.title