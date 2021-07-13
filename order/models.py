from django.db import models


class Category(models.Model):
	""" категории мороженого """
	name 		= models.CharField(max_length=200)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


class Icecream(models.Model):
	"""карточка мороженого"""
	name 		= models.CharField(max_length=200)
	description = models.TextField(blank=False, null=True)
	category	= models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT)
	active		= models.BooleanField(blank=True, default=False)
	image		= models.ImageField(upload_to='images/icecream')
	date_added	= models.DateTimeField(auto_now_add=True)
	price		= models.DecimalField(max_digits=5, decimal_places=0, default='2')

	class Meta:
		verbose_name = 'Мороженое'
		verbose_name_plural = 'Мороженое'

	def __str__(self):
		return self.name
