from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import localdate

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quit_date = models.DateField(localdate())
    daily_cost = models.DecimalField(max_digits=10, decimal_places=2,
                                     default=0.00)
    daily_smokes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Profile of {self.user.username}"
