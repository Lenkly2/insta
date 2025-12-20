from django import forms
from .models import Post, Coment, Massage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description","media"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "media": forms.ClearableFileInput(),
        }

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ["description","media"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "media": forms.ClearableFileInput(),
        }

class MassageForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ["to","massage"]
        to = forms.ChoiceField(choices=Massage.objects.all())
        widgets = {
            "massage": forms.TextInput(attrs={"class": "form-control"}),
        }

class Massage2Form(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ["massage"]
        widgets = {
            "massage": forms.TextInput(attrs={"class": "form-control"}),
        }
