from django.db import models

class Attemp(models.Model):
    TYPE_CHOICES = (
        ("SQ", "Squat"),
        ("BP", "Bench press"),
        ("DL", "Deadlift"),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
