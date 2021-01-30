from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Dinosaurs
from django import forms

class DinoForm(forms.ModelForm):
  class Meta:
    model = Dinosaurs
    fields = ['cover', 'name', 'lifespan', 'diet']
    labels = {'Image': 'cover', 'Name': 'name', 'lifespan': 'lifespan', 'Diet': 'diet'}

