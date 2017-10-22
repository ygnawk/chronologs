

import datetime    

from django.utils.timezone import now
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class Visit(models.Model):

    created   = models.DateTimeField('date created', auto_now_add=True)
    user      = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{str(self.user)}'s visit at {str(self.created)}"


class Entry(models.Model):

    doctor_first_name  = models.CharField(max_length=300)
    doctor_last_name  = models.CharField(max_length=300)
    hospital = models.CharField(max_length=300)

    visit     = models.ForeignKey(Visit, on_delete=models.PROTECT)
    created   = models.DateField('date created', auto_now_add=True)
    date_visit = models.DateField('date visit')
    doctor_note = models.TextField()
    edit_note  = models.TextField(default='new note')

    def __str__(self):
        return f"{str(self.created)} - {str(self.doctor_note)}"


class Medication(models.Model):

    TYPES = [
        ('surgery', 'surgery'),
        ('prescription', 'prescription'),
        ('other', 'other')
    ]

    entry           = models.ForeignKey(Entry, on_delete=models.PROTECT, default=None)
    identification  = models.CharField(max_length=500)
    medication_name = models.CharField(max_length=500)
    medication_type = models.CharField(max_length=500, choices=TYPES) 
    description     = models.TextField()
    
    models.ForeignKey(Entry, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.medication_name)



