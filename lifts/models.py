from django.db import models
from django.core.validators import FileExtensionValidator

class LiftType(models.TextChoices):
    SQUAT = 'przysiad', 'Przysiad'
    BENCH = 'wyciskanie', 'Wyciskanie'
    DEADLIFT = 'martwy_ciag', 'Martwy ciąg'

class LiftAttempt(models.Model):
    lift_type = models.CharField(max_length=20, choices=LiftType.choices)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True)
    video = models.FileField(
        upload_to='videos/',
        blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4','mov','webm','m4v'])]
    )

    class Meta:
        ordering = ['-date', '-weight_kg']

    def __str__(self):
        return f"{self.get_lift_type_display()} — {self.weight_kg} kg ({self.date})"
