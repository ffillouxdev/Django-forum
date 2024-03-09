from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify


class Topic(models.Model):
    IT= 'IT section'
    MATH = 'MATH section'
    PHYS = 'PHYS section'
    MEDICINE = 'Medicine section'
    SOCIOLOGY = 'Sociology section'
    DIVER = 'miscellaneous Topics'

    SECTION_CHOICES = [
        (IT, 'IT section'),
        (MATH, 'MATH section'),
        (PHYS, 'PHYS section'),
        (MEDICINE, 'Medicine section'),
        (SOCIOLOGY, 'Sociology section'),
        (DIVER, 'miscellaneous Topics'), 
    ]
    section = models.CharField(max_length=30, choices=SECTION_CHOICES, verbose_name='Section', default='None')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Reply(models.Model):
    topic = models.ForeignKey(Topic, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_at']