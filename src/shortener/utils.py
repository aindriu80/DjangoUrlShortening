
import random
import string

from django.conf import settings

SHORCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

#from shortener.models import KirrURL

def code_generator(size=SHORCODE_MIN, chars=string.ascii_lowercase + string.digits):
	# new_code=''
	# for_ in range(size):
	# 	new_code += random.choice(chars)
	# return new_code
	return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SHORCODE_MIN):
	new_code = code_generator(size=size)
	#print(instance)
	#print(instance.__class__)
	#print(instance.__class__.__name__)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code