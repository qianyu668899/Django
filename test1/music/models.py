from django.db import models

# Create your models here.
class Musician(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	instrument = models.CharField(max_length=100)

class Album(models.Model):
	artist = models.ForeignKey(Musician, verbose_name="Musician id")
	name = models.CharField(max_length=100)
	release_date = models.DateField()
	num_stars = models.IntegerField()

class Person(models.Model):
	SHIRT_SIZE=(
	('S', 'Small'),
	('M', 'Median'),
	('L', 'Large'),
	
	)
	name = models.CharField("person's name", max_length=100)
	shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)
	
	
	