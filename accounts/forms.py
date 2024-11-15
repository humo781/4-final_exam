from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'style': 'border: 2px solid #ccc;'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'style': 'border: 1px solid #ccc;'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'style': 'border: 2px solid #ccc;'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'style': 'border: 2px solid #ccc;'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'style': 'border: 2px solid #ccc;'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control-file', 'style': 'border: 2px solid #ccc;'})

    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'email', "password1", "password2", 'avatar')
