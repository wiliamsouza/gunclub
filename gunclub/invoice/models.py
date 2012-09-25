from django.db import models
from django.contrib.auth.models import User


class Invoice(models.Model):
    user = models.ForeignKey(User)
    payment_date = models.DateField()
    value = models.DecimalField(max_digits=5, decimal_places=2)
