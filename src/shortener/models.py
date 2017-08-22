from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True) 
	updated = models.DateTimeField(auto_now=True) #everytime the model is saved
	timestamp = models.DateTimeField(auto_now_add=True) #when model was created
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	#shortcode = models.CharField(max_length=15, null=True) Empty in databse is okay
	#shortcode = models.CharField(max_length=15, default='chedefaultshortcode')

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
