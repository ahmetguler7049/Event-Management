from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Category Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Event(models.Model):
    CATEGORIES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Health', 'Health'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=100, default="Untitled Event", verbose_name="Event Title")
    description = models.TextField(blank=True, null=True, verbose_name="Event Description")
    date = models.DateField(default=timezone.now, verbose_name="Event Date")
    time = models.TimeField(default=timezone.now, verbose_name="Event Time")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Event Category")

    def __str__(self):
        return f"{self.title} on {self.date}"

    class Meta:
        ordering = ['date', 'time']
        verbose_name = "Event"
        verbose_name_plural = "Events"
