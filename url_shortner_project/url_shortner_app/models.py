from django.db import models

# Create your models here.

class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.original_url