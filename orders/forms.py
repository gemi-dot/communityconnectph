from django import forms
from .models import WaterRefillRequest

class WaterRefillRequestForm(forms.ModelForm):
    class Meta:
        model = WaterRefillRequest
        fields = [
            'name',
            'phone_number',
            'address',
            'container_type',
            'quantity',
            'preferred_delivery_time',
            'notes',
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'notes': forms.Textarea(attrs={'rows': 2}),
            'preferred_delivery_time': forms.TextInput(attrs={'placeholder': 'e.g. Tomorrow morning'}),
        }
