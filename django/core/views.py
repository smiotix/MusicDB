from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from core.models import Album

# Create your views here.
class AlbumDetail(DetailView):
    model = Album
    
class AlbumList(ListView):
    model = Album