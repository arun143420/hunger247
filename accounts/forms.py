from django.contrib.auth.models import User
from django import forms
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.utils.translation import gettext as _
from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput
from accounts.models import ContactUs


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','id':'myInput'}))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=60, label='Email Address',)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2',]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.\
            update({

            'class': 'form-control',
            'id':'form',

        })
        self.fields['password1'].widget.attrs. \
            update({

            'class':'form-control',
            'name':'pass'

        })
        self.fields['username'].widget.attrs. \
            update({

            'class': 'form-control',


        })

        self.fields['password2'].widget.attrs. \
            update({

            'class': 'form-control',

        })
        self.fields['first_name'].widget.attrs. \
            update({

            'class': 'form-control',

        })
        self.fields['last_name'].widget.attrs. \
            update({

            'class': 'form-control',

        })


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs. \
            update({

            'class': 'form-control',
            'id':'phone',



        })
        self.fields['address'].widget.attrs. \
            update({

            'class': 'form-control',

        })
        self.fields['pincode'].widget.attrs. \
            update({

            'class': 'form-control',




        })
        self.fields['area'].widget.attrs. \
            update({

            'class': 'form-control',

        })
        self.fields['land_mark'].widget.attrs. \
            update({

            'class': 'form-control',

        })
        self.fields['tc'].widget.attrs. \
            update({

            'required':'true',

        })




class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['user']


    def __init__( self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs. \
            update({

            'class': 'form-control',
            'id':'phone',




        })
        self.fields['email'].widget.attrs. \
            update({

            'class': 'form-control',

        })
        self.fields['name'].widget.attrs. \
            update({

            'class': 'form-control',




        })
        self.fields['Comment_and_Suggestion'].widget.attrs. \
            update({

            'class': 'form-control',




        })


class SignUpEditForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=60, label='Email Address',)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(SignUpEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.\
            update({

            'class': 'form-control',
            'id':'form',

        })

        self.fields['username'].widget.attrs. \
            update({

            'class': 'form-control',


        })


        self.fields['first_name'].widget.attrs. \
            update({

            'class': 'form-control',

        })
        self.fields['last_name'].widget.attrs. \
            update({

            'class': 'form-control',

        })

