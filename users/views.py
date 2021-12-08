from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import User


class UserListView(ListView):
    template_name = "users/users_list.html"
    model = User


class UserDetailView(DetailView):
    template_name = "users/user_detail.html"
    model = User


class UserCreateView(CreateView):
    template_name = "users/user_create.html"
    model = User
    fields = []


class UserUpdateView(UpdateView):
    template_name = "users/user_update.html"
    model = User
    fields = []


class UserDeleteView(DeleteView):
    template_name = "users/user_delete.html"
    model = User
    success_url = reverse_lazy("users_list")
# Create your views here.

# Create your views here.
