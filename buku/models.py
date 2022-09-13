from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    writer = models.CharField(max_length=201)

    def __str__(self):
        return self.writer


class Book(models.Model):
    category_choice = (
        ('politics', 'Politics'),
        ('technology', 'Technology'),
        ('literature', 'Literature'),
        ('economy', 'Economy'),
        ('health', 'Health'),
    )
    category = models.CharField(
        max_length=51, blank=True, null=True, choices=category_choice)
    title = models.CharField(max_length=201)
    description = models.TextField(max_length=9501, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    author_name = models.ForeignKey(
        Author, on_delete=models.PROTECT, default=1)
    published = models.DateTimeField(default=timezone.now)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        return reverse('detailbook', args=[str(self.pk)])
