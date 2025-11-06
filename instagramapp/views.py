from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView,ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from .models import Post, Coment, CustomUser
from .forms import PostForm
from django import forms
# Create your views here.
class ListPostView(ListView):
    model=Post
    template_name="listpost.html"
    context_object_name="lp"

class CreatePostView(CreateView):
    model = Post
    template_name = "createpost.html"
    form_class = PostForm
    success_url = reverse_lazy("listpost")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePostView(DeleteView):
    model = Post

class UpdatePostView(UpdateView):
    model = Post

class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name = "user"

class CreateCommentView(CreateView):
    model = Coment

class CustomUserCreatinForm(UserCreationForm):
    avatar = forms.ClearableFileInput()
    class Meta:
        model = CustomUser
        fields = ["username","avatar","password1", "password2"]

class RegisterView(FormView):
    template_name="auth/register.html"
    form_class = CustomUserCreatinForm
    success_url = reverse_lazy("listpost")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name="auth/login.html"
    success_url = reverse_lazy("listpost")

class UserLogoutView(LogoutView):
    success_url = reverse_lazy("listpost")

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = "createpost.html"
    fields = ["avatar"]
    success_url = reverse_lazy("profile")