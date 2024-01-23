from django.db import models


class Course(models.Model):
    rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
