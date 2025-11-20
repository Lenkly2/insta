from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView,ListView, FormView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from .models import Post, Coment, CustomUser, Massage
from .forms import PostForm,ComentForm, MassageForm
from django import forms
import datetime
# Create your views here.
class BaseView(TemplateView):
    template_name="base.html"

class ListPostView(LoginRequiredMixin, ListView):
    redirect_field_name = reverse_lazy("listpost")
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

class DetailPostView(DetailView):
    model = Post
    template_name = "postdetail.html"
    context_object_name = "detailpost"

    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        context['coment'] = Coment.objects.filter(post = self.object)
        return context
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "ducomfirm.html"
    success_url = reverse_lazy("listpost")

class UpdatePostView(UpdateView):
    model = Post
    template_name = "ducomfirm.html"
    success_url = reverse_lazy("listpost")
    
class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name = "user"

class CreateCommentView(CreateView):
    model = Coment
    template_name = "commentcreate.html"
    form_class = ComentForm
    success_url = reverse_lazy("listpost")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        post = self.kwargs["pk"]
        form.instance.post = Post.objects.get(id=post)
        return super().form_valid(form)
    
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

class UserLogoutView(LogoutView):
    ...

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = "createpost.html"
    fields = ["avatar"]
    success_url = reverse_lazy("profile")

class MassageListView(ListView):
    model = Massage
    template_name = "massagelist.html"

    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        context['ml'] = Massage.objects.filter(to = self.request.user)
        # context['ml1'] = Massage.objects.filter(by = self.request.user)
        return context

class CreateMassageView(CreateView):
    model = Massage
    template_name = "massagecreate.html"
    form_class = MassageForm
    success_url = reverse_lazy("listpost")

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

class DetailMassageView(DetailView):
    model = Massage
    template_name = "massagedetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ml'] = Massage.objects.filter(to = self.request.user)
        context['ml1'] = Massage.objects.filter(by = self.kwargs['pk'])
        return context

# def LikesAddView(request, pk):
#     post = get_object_or_404(Portfolio, id=request.POST.get('like_id'))
#     post.likes.add(request.user)
#     return redirect("port_list")