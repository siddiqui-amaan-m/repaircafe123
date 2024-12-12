from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'plz', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # To render password field as input type="password"
        }
