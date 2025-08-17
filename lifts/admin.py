from django.contrib import admin
from .models import LiftAttempt

@admin.register(LiftAttempt)
class LiftAttemptAdmin(admin.ModelAdmin):
    list_display = ('date', 'lift_type', 'weight_kg')
    list_filter = ('lift_type', 'date')
    search_fields = ('notes',)
