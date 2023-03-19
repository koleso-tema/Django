from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Author, Category


class NewsForm(forms.ModelForm):
    author = forms.ModelChoiceField(label='Aвтор', queryset=Author.objects.all())
    title = forms.CharField(label='Заголовок')
    postCategory = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all())


    class Meta:
        model = Post
        fields = [
            'title',
            'categoryType',
            'author',
            'text',


        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 50:
            raise ValidationError({
                "text": "Слишком короткий текст."
            })

        return cleaned_data
