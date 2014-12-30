from django import forms


class ReadPageForm(forms.Form):
    url = forms.URLField(required=True)
