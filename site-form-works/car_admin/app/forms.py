from django import forms
from .models import Car, Review

from ckeditor.widgets import CKEditorWidget


class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label='Обзор')

    class Meta:
        model = Review
        fields = ['car', 'title', 'text']
