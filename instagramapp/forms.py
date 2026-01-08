from django import forms
from .models import Post, Coment, Massage,Subscribers,CustomUser

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

        widgets = {
                    "massage": forms.TextInput(attrs={"class": "form-control"}),
                }
        
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        a = Subscribers.objects.filter(follower=user)
        m = list()
        for i in a:
            m.append(i.following.id)

        self.fields["to"].queryset = CustomUser.objects.filter(id__in = m)

        

class Massage2Form(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ["massage","media"]
        widgets = {
            "massage": forms.TextInput(attrs={"class": "form-control"}),
            "media": forms.ClearableFileInput(),
        }


class PMForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ["to"]

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        a = Subscribers.objects.filter(follower=user)
        m = list()
        for i in a:
            m.append(i.following.id)

        self.fields["to"].queryset = CustomUser.objects.filter(id__in = m)

        