from django.utils import timezone
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    due_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    def _str_(self):
        return self.title

    def status(self):
        duration = self.due_date - timezone.now()
        duration_in_s = duration.total_seconds()
        days = duration.days
        days = divmod(duration_in_s, 86400)[0]
        
        if self.completed == True:
            return 'Completed'

        if days <= 0:
            return 'Overdue'
        
        if days < 7:
            return 'Due Soon'

        return 'Not Urgent'