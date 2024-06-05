from django import forms
from datetime import datetime


class ToDoForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Title",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=255,
        label="Description",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    start_date = forms.DateTimeField(
        initial=datetime.now,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    end_date = forms.DateTimeField(
        initial=datetime.now,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    complete = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class UserForm(forms.Form):
    username = forms.CharField(max_length=100, label="User Name")
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)
