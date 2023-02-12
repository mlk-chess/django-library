from django import forms
from .models import readingGroup
from book.models import Book


class GroupForm(forms.ModelForm):
    book_id = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        label='Livre',
        empty_label=None,
    )

    class Meta:
        model = readingGroup
        fields = ['name', 'description', 'date', 'book_id']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
        }
