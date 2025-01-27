from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/CookieStand_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/CookieStand_detail.html"
    model = CookieStand


class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/CookieStand_update.html"
    model = CookieStand
    fields = "__all__"


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/CookieStand_create.html"
    model = CookieStand
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/CookieStand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("CookieStand_list")
