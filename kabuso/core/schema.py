from django import forms


class RequestPageSchema(forms.Form):
    page_url = forms.URLField()
    title = forms.CharField(max_length=255, required=False)
    summary_image_url = forms.URLField(required=False)
    description = forms.CharField(max_length=4095, required=False)
