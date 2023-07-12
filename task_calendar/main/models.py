from django.db import models

class Task(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    URGENCY_CHOICES = (
        ("Low","Low"),
        ("Mid","Mid"),
        ("High","High"),
        ("GET IT DONE", "GET IT DONE"),
    )

    PROGRESS_CHOICES = (
        ("Just Starting","Just Starting"),
        ("25%","25%"),
        ("50%","50%"),
        ("75%","75%"),
        ("Finished", "Finished"),
    )

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=155)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES)
    progress = models.CharField(max_length=20, choices=PROGRESS_CHOICES)

    def __str__(self):
        return self.title
