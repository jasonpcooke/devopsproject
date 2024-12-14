from django.db import models
from django.contrib.auth.models import User

class TicketStatus(models.TextChoices):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    IN_REVIEW = 'In Review'
    DONE = 'Done'

class Ticket(models.Model):
    title = models.CharField(max_length=100)    
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=25,
        choices=TicketStatus.choices,
        default=TicketStatus.TO_DO,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title