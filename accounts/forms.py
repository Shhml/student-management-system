from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from courses.models import Course, Department
from django.contrib.auth.forms import PasswordChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control bg-secondary text-light border-0',
            'placeholder': 'Enter username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control bg-secondary text-light border-0',
            'placeholder': 'Enter password',
            'autocomplete': 'new-password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control bg-secondary text-light border-0',
            'placeholder': 'Confirm password',
            'autocomplete': 'new-password'
        })

class StudentProfileForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select bg-secondary text-light border-0'}),
        empty_label="Select a course"
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select bg-secondary text-light border-0'}),
        empty_label="Select a department"
    )
    batch_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control bg-secondary text-light border-0',
            'min': 2000,
            'max': 2030,
            'placeholder': 'Enter batch year (e.g., 2023)'
        }),
        help_text="Enter the batch year (e.g., 2023).",
        min_value=2000,
        max_value=2030
    )

class StaffProfileForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select bg-secondary text-light border-0'}),
        empty_label="Select a department",
        required=False  # Make optional
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select bg-secondary text-light border-0'}),
        empty_label="Select a course",
        required=False  # Make optional
    )




class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control bg-secondary text-light border-0',
            'placeholder': 'Enter your current password'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control bg-secondary text-light border-0',
            'placeholder': 'Enter new password'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control bg-secondary text-light border-0',
            'placeholder': 'Confirm new password'
        })


