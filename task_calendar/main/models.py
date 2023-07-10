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

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    urgency = models.IntegerField()

    def __str__(self):
        return self.title
