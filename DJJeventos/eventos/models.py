from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

	

class reserva(models.Model):
	"""Model representing an reserva."""
	codigo_reserva = models.CharField(max_length=10)
	fecha_evento = models.DateField(null=True, blank=True)
	nom_cliente = models.CharField(max_length=200)
	apell_cliente = models.CharField(max_length=200)
	celu_cliente = models.CharField(max_length=10)
	email = models.CharField(max_length=200)
	cant_personas = models.IntegerField(default=0)
	total = models.IntegerField(default=0)

	def __str__(self):
		return self.codigo_reserva

