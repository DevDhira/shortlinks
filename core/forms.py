from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField( 
        label= 'Password',
        widget= forms.PasswordInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-blue-500'})
     )

    password2 = forms.CharField( 
        label= 'Confirm Password',
        widget= forms.PasswordInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-blue-500'})
     )

    class Meta:
        model = User
        fields = ('username','email' ,'password1', 'password2')
        widget = {
            'username':forms.TextInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-blue-500'}),
            'email':forms.TextInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-blue-500'}),
        }
