from django.db import models

# Create your models here.
class category(models.Model):
    end_year = models.IntegerField()
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    start_year = models.IntegerField()
    impact = models.IntegerField()
    added = models.CharField(max_length=100)
    published = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    likelihood = models.IntegerField()
    def __str__(self):
        return self.sector