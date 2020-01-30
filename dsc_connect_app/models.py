from django.db import models

STATUS_CHOICES = [
	('0','draft'),
	('1','published'),
	]


class Dsc(models.Model):
	
	
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	status = models.CharField(max_length=1, choices = STATUS_CHOICES)
	lead = models.CharField(max_length = 200 , blank = False)
	name = models.CharField(max_length=50)
	gmail = models.EmailField(blank=True)
	cover = models.ImageField(upload_to='images/')
	city = models.CharField(max_length=300)
	state = models.CharField(max_length=300)
	team_size = models.IntegerField()
	established_on =models.DateField(auto_now=False)
	created_on = models.DateTimeField(auto_now_add=False)
	updated_on = models.DateTimeField(auto_now=True)
	website = models.URLField(blank=True)
	github = models.URLField(blank=True)
	medium = models.URLField(blank=True)
	facebook = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	linkedin = models.URLField(blank=True)
	instagram = models.URLField(blank=True)
	youtube = models.URLField(blank=True)
	behance = models.URLField(blank=True)
	custom = models.URLField(blank=True)
	"""
		add fields here!!
	"""


	def __str__(self):
		return self.name


