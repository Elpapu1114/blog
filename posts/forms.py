from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Tu nombre", "autocomplete": "name"}),
            "body": forms.Textarea(attrs={"placeholder": "Escribí tu comentario", "rows": 4}),
        }