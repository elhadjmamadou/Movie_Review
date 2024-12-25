from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser
from .forms import SignupForm
from django.http import HttpResponse
from django.urls import reverse_lazy


class SignupView(CreateView):
    model = CustomUser 
    form_class = SignupForm
    template_name = "accounts/signup.html"
    context_object_name = "form"
    success_url = reverse_lazy("login")

    # def form_valid(self, form):
    #     self.object = form.save()
    #     return HttpResponse("success")
