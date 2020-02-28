from django.db import models

# Create your models here.

class Album(models.Model):
    POP = 0
    JAZZ = 1
    CLASSIC = 2
    ROCK = 3
    HIPHOP = 4
    EDM = 5
    ETC = 6
    Tracks = list()
    GENRE = ((POP, 'POP MUSIC'),
             (JAZZ, 'JAZZ'),
             (CLASSIC, 'CLASSIC MUSIC'),
             (ROCK, 'ROCK'),
             (HIPHOP, 'HIPHOP'),
             (EDM, 'EDM'),
             (ETC, 'OTHER'),
             )
    album_title = models.CharField(max_length=140)
    year = models.PositiveIntegerField()
    genre = models.IntegerField(choices=GENRE,default=POP)
    criticism = models.TextField()
    spotify = models.URLField(blank=True)
       
    def __str__(self):
        return '{} {}'.format(self.album_title, self.year)
    

    