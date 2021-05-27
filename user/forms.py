from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
    },
        max_length=32, label='사용자 이름'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    #유효성 검사
    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')

        if userid and password:
            try:
                user = User.objects.get(userid=userid)
            except User.DoesNotExist:
                self.add_error('userid', '아이디가 없습니다')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다')


class RegisterForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required': 'please enter the userid'
        },
        max_length=32, label='사용자 이름'
    )
    password = forms.CharField(
        error_messages={
            'required': 'please enter the password'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': 'please enter the re_password'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )
    email = forms.EmailField(
        error_messages={
            'required': 'please enter the email'
        },
        max_length=64, label='이메일'
    )
    def clean(self):#유효성 검사
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        email = cleaned_data.get('email')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'password, re_password incorrect')
                self.add_error('re_password', 'password, re_password incorrect')
