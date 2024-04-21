from typing import Any
from django import forms


class WarmUpOneForm(forms.Form):
    num = forms.IntegerField()

class WarmUpTwoForm(forms.Form):
    string = forms.CharField()