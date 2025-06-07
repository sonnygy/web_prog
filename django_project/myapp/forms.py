from django import forms
from .models import Comment
from datetime import datetime
import re

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'placeholder': 'Комментарий'}),
            'rating': forms.RadioSelect(),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[А-Яа-яA-Za-z\s]+$', name):
            raise forms.ValidationError("Имя должно содержать только буквы.")
        return name

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text.strip():
            raise forms.ValidationError("Комментарий не должен быть пустым.")
        return text


