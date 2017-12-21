from django.db import models
from django.utils import timezone


class Ideas(models.Model):
    author = models.ForeignKey('auth.User')
    date = models.CharField(max_length=200)
    costs = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    keyword = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.date
