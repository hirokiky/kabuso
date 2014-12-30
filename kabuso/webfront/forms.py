from django import forms


class ReadPageForm(forms.Form):
    url = forms.URLField(required=True)


class PageDetailForm(forms.Form):
    sorted_by = forms.ChoiceField(choices=(('top', 'Top'), ('newest', 'Newest')))
