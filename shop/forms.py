from django import forms
from shop.models import Product, Message, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
INPUT_CLASSES = 'form-control'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин',
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Пароль',
        'class': 'form-control',
        'type': 'password'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин',
        'class': 'form-control',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': 'form-control',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',
        'class': 'form-control',
    }))


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class UsersOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('item', 'size', 'name', 'email', 'payment', 'address')
        widgets = {
            'item': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'size': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'payment': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }


class UsersMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваш email'
            }),
            'message': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваше сообщение'
            })
        }
