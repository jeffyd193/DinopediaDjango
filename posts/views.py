from typing import List
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Dinosaurs
from .forms import DinoForm

# Create your views here.
class HomePageView(ListView):
    model = Dinosaurs
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Dinosaurs
    form_class = DinoForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
  