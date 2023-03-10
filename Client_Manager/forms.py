from django import forms

from Client_Manager.models import Client, Comment


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Введите логин."
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Введите пароль."
        })
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }


class LandingForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "name",
            'placeholder': "Введите имя:"
        })
    )
    lastName = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "lastName",
            'placeholder': "Введите фамилию"
        })
    )
    phone = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control md-textarea",
            'id': "phone",
            'placeholder': "Введите номер телефона."
        })
    )
    email = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'id': "email",
            'placeholder': "Введите email:"
        })
    )

