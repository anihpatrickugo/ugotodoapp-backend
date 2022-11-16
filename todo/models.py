from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Todo(models.Model):
    "This is the database schema for the todos."

    tittle = models.CharField(max_length=100)
    body   = models.TextField()
    date   = models.DateTimeField(auto_now_add=True)
    done   = models.BooleanField(default=False)
    user   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.tittle