'''from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    topic = models.CharField('Topic', max_length=256, default=None, blank=False, null=False)
    message = models.TextField('Message', default=None, blank=True, null=True)
    created_at = models.DateTimeField('Created at',auto_now_add=True, blank=False, null=False)
    answered_at = models.DateTimeField('Answered at',default=None, blank=True, null=True)
    answer = models.TextField('Answer', default=None, blank=True, null=True)
    CHOICES = (
        ('1', 'User Ticket'),
        ('2', 'Test Error'),
        ('3', 'Test Warninge'),
        ('4', 'Test Information'),
    )
    type = models.CharField('Type', max_length=2, choices=CHOICES, default=None, blank=False, null=False)
    is_done = models.NullBooleanField('Is Done', default=False, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    answered_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)'''
