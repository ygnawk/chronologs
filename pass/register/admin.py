from django.contrib import admin

# Register your models here.
from .models import Entry, Visit, Medication

admin.site.register(Entry)
admin.site.register(Visit)
admin.site.register(Medication)

