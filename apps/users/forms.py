# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/4/12 23:31'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)