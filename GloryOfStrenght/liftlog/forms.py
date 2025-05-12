from django import forms
from .models import LiftVideo

class LiftVideoForm(forms.ModelForm):
    class Meta:
        model = LiftVideo
        fields = ['title', 'lift_type', 'weight', 'video']