
from django import forms
from .models import Link
from linkbox_tools import normalize_url, is_valid_url


class LinkForm(forms.ModelForm):
    url = forms.CharField(
        max_length=2048,
        widget=forms.TextInput(attrs={
            'placeholder': 'example.com',
        }),
    )

    class Meta:
        model = Link
        fields = ['title', 'url', 'description', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_url(self):
        raw_url = self.cleaned_data['url']

        try:
            normalized = normalize_url(raw_url)
        except ValueError as error:
            raise forms.ValidationError(str(error))

        if not is_valid_url(normalized):
            raise forms.ValidationError(
                'Enter a valid HTTP or HTTPS URL.'
            )

        return normalized
