from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class News(models.Model):
    subject = models.TextField()
    news_text = models.TextField()
    news_date = models.DateTimeField()

    def __str__(self):
        return self.subject

    def date_published(self):
        return self.news_date >= timezone.now() - timedelta(days=1)


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class npa_documents(models.Model):
    label = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.label

class ts_orm(models.Model):
    name = models.CharField(max_length=255)
    note = models.CharField(max_length=255)

    def __str__(self):
        return self.name