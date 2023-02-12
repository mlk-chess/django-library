from django import forms
from .models import readingGroup


class GroupForm(forms.ModelForm):
    class Meta:
        model = readingGroup
        fields = ['name', 'description', 'date']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
        }
