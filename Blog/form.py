#!/usr/bin/env python
#--*-- coding:utf-8 --*--
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length= 100)
    e_mail = forms.EmailField(required=True)
    message = forms.EmailField()