from django.db import models

class LiftVideo(models.Model):
    LIFT_CHOICES = [
        ('SQ', 'Squat'),
        ('BP', 'Bench press'),
        ('DL', 'Deadlift'),
    ]

    title = models.CharField(max_length=100)
    lift_type = models.CharField(max_length=2, choices=LIFT_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    video = models.FileField(upload_to='videos/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_lift_type_display()}"
    