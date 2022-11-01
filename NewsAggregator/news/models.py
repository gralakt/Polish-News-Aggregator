from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True)  # Title of the article
	image = models.URLField(null=True, blank=True)  # URL of the article image
	url = models.TextField(null=True, blank=True)  # Title of the article

	def __str__(self):
		return self.title