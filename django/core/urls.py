from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
        path('albums',
        views.AlbumList.as_view(),
        name='AlbumList'),
        path('album/<int:pk>',
             views.AlbumDetail.as_view(),
             name='AlbumDetail'),
]