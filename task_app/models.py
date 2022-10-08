from django.utils import timezone
from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_NOT_URGENT = "Not"
    STATUS_DUE_SOON = "Soon"
    STATUS_OVERDUE = "Over"
    STATUS_COMPLETED= "Complete"

    STATUS_CHOICES = [
        (STATUS_NOT_URGENT, 'Not Urgent'),
        (STATUS_DUE_SOON, 'Due Soon'),
        (STATUS_OVERDUE, 'Overdue'),
        (STATUS_COMPLETED, 'Completed')
    ]    

    title = models.CharField(max_length=120)
    description = models.TextField()
    due_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=75, choices=STATUS_CHOICES, default=STATUS_NOT_URGENT)


    def _str_(self):
        return self.title

    def save(self, *args, **kwargs):
        duration = self.due_date - timezone.now()
        duration_in_s = duration.total_seconds()
        days = duration.days
        days = divmod(duration_in_s, 86400)[0]
        
        if days <= 0:
            self.status = self.STATUS_OVERDUE
        
        elif days < 7:
            self.status = self.STATUS_DUE_SOON

        elif self.completed == True:
            self.status = self.STATUS_COMPLETED

        super().save(*args, **kwargs)