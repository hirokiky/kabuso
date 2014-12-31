import floppyforms as forms


class ReadPageForm(forms.Form):
    url = forms.URLField(required=True)


class PageDetailForm(forms.Form):
    sorted_by = forms.ChoiceField(choices=(('top', 'Top'), ('recent', 'Recent')))


class CommentPageForm(forms.Form):
    body = forms.CharField(max_length=4095,
                           widget=forms.Textarea(attrs={'rows': 3,
                                                        'cols': 43,
                                                        'placeholder': 'Leave your comment...'}))
