from django import forms
from .models import Post, Coment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description","media"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "media": forms.ClearableFileInput(),
        }