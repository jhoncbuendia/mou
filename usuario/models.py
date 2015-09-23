from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
	user = models.ForeignKey(User)
	auspiciador = models.CharField( max_length = 20)

	def __unicode__(self):
		return self.user.username