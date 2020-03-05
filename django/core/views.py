from django.shortcuts import render
from django.views.generic import ListView
from core.models import Album

# Create your views here.
class AlbumList(ListView):
    model = Album