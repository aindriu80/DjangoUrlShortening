import random
import string
from django.db import models

#from __future__ import unicode_literals

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	# new_code=''
	# for_ in range(size):
	# 	new_code += random.choice(chars)
	# return new_code
	return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True) 
	updated = models.DateTimeField(auto_now=True) #everytime the model is saved
	timestamp = models.DateTimeField(auto_now_add=True) #when model was created
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	#shortcode = models.CharField(max_length=15, null=True) Empty in databse is okay
	#shortcode = models.CharField(max_length=15, default='chedefaultshortcode')

	def save(self, *args, **kwargs):
		print("something")
		self.shortcode = code_generator()
		super(KirrURL, self).save(*args, **kwargs)

	# def my_save(self):
	# 	self.save()	


	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)