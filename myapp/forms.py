from django import forms
from .models import Application
from datetime import datetime

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'car': forms.TextInput(attrs={'class': 'form-input'}),
            'year': forms.NumberInput(attrs={'class': 'form-input'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-textarea'}),
            'time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'notification': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.istitle():
            raise forms.ValidationError("Имя должно начинаться с заглавной буквы.")
        if len(name) < 3:
            raise forms.ValidationError("Имя должно быть не меньше 3 символов.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit() and not phone.startswith('+'):
            raise forms.ValidationError("Телефон должен содержать только цифры или начинаться с '+'.")
        if len(phone) < 10 or len(phone) > 15:
            raise forms.ValidationError("Телефон должен быть от 10 до 15 символов.")
        return phone

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year is not None:
            current_year = datetime.now().year
            if year < 1900 or year > current_year:
                raise forms.ValidationError("Введите корректный год выпуска.")
        return year
