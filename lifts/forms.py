from django import forms
from .models import LiftAttempt

class LiftAttemptForm(forms.ModelForm):
    class Meta:
        model = LiftAttempt
        fields = ['lift_type', 'weight_kg', 'date', 'notes']
        widgets = {
            'lift_type': forms.Select(attrs={'class': 'input'}),
            'weight_kg': forms.NumberInput(attrs={'step': '0.5', 'class': 'input', 'placeholder': 'np. 200.0'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'class': 'input', 'placeholder': 'Opcjonalne notatki…'}),
        }
        labels = {
            'lift_type': 'Rodzaj boju',
            'weight_kg': 'Ciężar (kg)',
            'date': 'Data',
            'notes': 'Notatki',
        }
