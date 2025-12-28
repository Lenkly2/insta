from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView,ListView, FormView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from .models import Post, Coment, CustomUser, Massage,Subscribers
from .forms import PostForm,ComentForm, MassageForm, Massage2Form
from django import forms
from django.db.models import Q
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
    template_name = "mcpcreate.html"
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sblog'] = Post.objects.filter(author = self.kwargs['pk'])
        context['folowing'] = Subscribers.objects.filter(follower=self.kwargs['pk'])
        context['folowing'] = context['folowing'].count()
        context['folower'] = Subscribers.objects.filter(following=self.kwargs['pk'])
        context['folower'] = context['folower'].count()
        context['sblogcount'] = context['sblog'].count()
        return context

class CreateCommentView(CreateView):
    model = Coment
    template_name = "mcpcreate.html"
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
        fields = ["username","first_name","avatar","password1", "password2"]

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
    template_name = "mcpcreate.html"
    fields = ["avatar"]

    def get_success_url(self):
        # str(self.request.user.pk)+"/profile/"
        return reverse_lazy("profile",args=[self.request.user.pk])
    # success_url = reverse_lazy("profile",pk=b)

class MassageListView(ListView):
    model = Massage
    template_name = "massagelist.html"
    context_object_name = "ml"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Massage.objects.filter(Q(by=self.request.user) | Q(to=self.request.user))
        chat = {}
        for m in queryset:
            if m.by == self.request.user:
                compa = m.to
            else:
                compa = m.by

            if compa.id not in chat:
                chat[compa.id] = m

        return chat.values()

class CreateMassageView(CreateView):
    model = Massage
    template_name = "mcpcreate.html"
    form_class = MassageForm
    success_url = reverse_lazy("massagelist")

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

class DetailMassageView(DetailView):
    model = Massage
    template_name = "massagedetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ml'] = Massage.objects.filter(to = self.request.user)
        context['who'] = self.kwargs['pk']
        context['ml1'] = Massage.objects.filter(by = self.request.user)
        return context

class CreateMassage2View(CreateView):
    model = Massage
    template_name = "mcpcreate.html"
    form_class = Massage2Form
    success_url = reverse_lazy("massagelist")

    def form_valid(self, form, **kwargs):
        form.instance.by = self.request.user 
        form.instance.to = CustomUser.objects.get(pk = self.kwargs['pk'])
        return super().form_valid(form)

class SearchTemplateView(TemplateView):
    template_name = "search.html"

class SearchListView(ListView):
    model = Post
    template_name = "listpost.html"
    context_object_name = 'lp'
    def get_queryset(self):
        sin = self.request.GET.get('searchinput')
        data = Post.objects.filter(description__icontains=sin)
        return data
    

def USubribe(request,pk):
    fol = CustomUser.objects.get(pk = pk)
    prot = Subscribers.objects.get(following=fol,follower=request.user)
    if prot:
        pass
    else:
        us = Subscribers.objects.create(following=fol,follower=request.user)
        us.save()
    return redirect("listpost")

def ThemeChange(request,pk):
    us = CustomUser.objects.get(pk=pk)
    if us.theme == 0:
        us.theme = 1
    else:
        us.theme = 0
    us.save()
    return redirect("listpost")

# def LikesAddView(request, pk):
#     post = get_object_or_404(Portfolio, id=request.POST.get('like_id'))
#     post.likes.add(request.user)
#     return redirect("port_list")