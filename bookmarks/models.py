from django.db import models

class Link(models.Model):
    class Category(models.TextChoices):
        PROGRAMMING = 'Programming', 'Programming'
        DOCUMENTATION = 'Documentation', 'Documentation'
        SCHOOL = 'School', 'School'
        ARTICLES = 'Articles', 'Articles'
        TOOLS = 'Tools', 'Tools'
        OTHER = 'Other', 'Other'

    title = models.CharField(max_length=150)
    url = models.URLField(max_length=2048)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.url})"
