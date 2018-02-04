from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return (self)