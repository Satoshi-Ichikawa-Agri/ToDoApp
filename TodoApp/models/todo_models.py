""" todoモデル
"""
from django.db import models


class Todo(models.Model):
    """todoテーブル
    """
    summary = models.CharField(max_length=50)
    detail = models.CharField(max_length=100, blank=True)
    limit = models.DateField()
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.summary
