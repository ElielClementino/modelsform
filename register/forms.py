from logging import PlaceHolder
from tkinter import Widget
from django import forms


class Formulario(forms.Form):
    usuario = forms.CharField(max_length=80,PlaceHolder='digite um email ou nome de usuario')

    def __init__(self):
        return self.usuario