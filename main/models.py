from django.db import models

# Create your models here.
class Tutorial(models.Model):
	web_title = models.CharField(max_length=200)
	web_content = models.TextField()
	web_published = models.DateTimeField("date published")

	def __str__(self):
		return self.web_title
