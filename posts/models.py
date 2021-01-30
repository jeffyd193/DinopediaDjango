from django.db import models
from django.contrib import admin
from django.forms import ModelForm

# Create your models here.
class Dinosaurs(models.Model):
    cover = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=40)
    lifespan = models.SmallIntegerField()
    DIET = (
        ('Herbivore', 'Herbivore'),
        ('Carnivore', 'Carnivore'),
        ('Omnivore', 'Omnivore'),
    )
    diet = models.CharField(max_length=10, choices=DIET, default='O')

    def __str__(self):
        return self.name

note = models.TextField(default='', blank=True)