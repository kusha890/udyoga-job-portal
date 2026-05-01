from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-2 border rounded mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border rounded mb-2'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['cgpa', 'branch', 'skills', 'resume']

        widgets = {
            'cgpa': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded mb-2'}),
            'branch': forms.TextInput(attrs={'class': 'w-full p-2 border rounded mb-2'}),
            'skills': forms.Textarea(attrs={'class': 'w-full p-2 border rounded mb-2'}),
            'resume': forms.FileInput(attrs={'class': 'w-full mb-2'}),
        }