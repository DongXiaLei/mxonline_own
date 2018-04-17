# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/4/12 23:31'
# 用来form验证

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

