from django import forms
from .models import PrayerRequest, NewsLetterUsers
from phonenumber_field.formfields import PhoneNumberField

class PrayerRequestForm(forms.ModelForm):
    
    class Meta:
        model = PrayerRequest
        fields = '__all__'

class NewsLetterUsersForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetterUsers
        fields = '__all__'
        widgets = {
            "email": forms.EmailInput(attrs={'placeholder': 'Email'})
        }
