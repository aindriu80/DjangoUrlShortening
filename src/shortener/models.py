
from django.db import models
from .utils import code_generator, create_shortcode


class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items=None):		
		qs = KirrURL.objects.filter(id__gte=1)	
		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
		new_codes = 0
		for q in qs:			
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save()
			new_codes +=1
		return "New codes mades: {i}".format(i=new_codes)


# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True, blank=True) 
	updated = models.DateTimeField(auto_now=True) #everytime the model is saved
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True) #when model was created
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	#shortcode = models.CharField(max_length=15, null=True) Empty in databse is okay
	#shortcode = models.CharField(max_length=15, default='chedefaultshortcode')
	#
	
	objects = KirrURLManager()
	some_random = KirrURLManager()



	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(KirrURL, self).save(*args, **kwargs)

	# class Meta:
	#	ordering = '-id'

	# def my_save(self):
	# 	self.save()	


	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
