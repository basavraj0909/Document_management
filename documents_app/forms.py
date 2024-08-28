from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    # todo: multiple file upload
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Document
        fields = ['file', 'name']
