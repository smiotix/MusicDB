from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
        path('albums',
        view.AlbumList.as_view(),
        name='AlbumList'),
]