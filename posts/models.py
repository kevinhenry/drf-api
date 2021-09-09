from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Plog(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    header = models.CharField(max_length=64)
    note = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.header
