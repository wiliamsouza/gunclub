import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from member.models import Profile

class Invoice(models.Model):
    user = models.ForeignKey(User)
    payment_date = models.DateField(blank=True, null=True)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=5, decimal_places=2)
