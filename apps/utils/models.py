from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_status = models.BooleanField(default=True)

    class Meta:
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']