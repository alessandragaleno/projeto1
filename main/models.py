
from django.db import models

# Create your models here.
class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)

class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE,related_name="items")
    text = models.TextField("descrição de item")
    complete = models.BooleanField(default=False)