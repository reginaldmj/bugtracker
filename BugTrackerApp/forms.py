from django import forms
from BugTrackerApp.models import MyUser, MyTicket
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password','display_name', 'age']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class AddBugTicketForm(forms.ModelForm):
    class Meta:
        model = MyTicket
        fields = ('title', 'description',)

class MyUserCreationForm(UserCreationForm):
    display_name = forms.CharField(max_length=20)

    class Meta:
        model = MyUser
        fields = ('username', 'display_name', 'age')

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('username',)

