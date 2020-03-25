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
    artist = models.ForeignKey(to='Artist',on_delete=models.SET_NULL,related_name='created',null=True,blank=True)
    album_title = models.CharField(max_length=140)
    year = models.PositiveIntegerField()
    genre = models.IntegerField(choices=GENRE,default=POP)
    criticism = models.TextField()
    spotify = models.URLField(blank=True)
       
    class Meta:
        ordering = ('year', 'album_title')
    def __str__(self):
        return '{} {}'.format(self.album_title, self.year)
    
class Artist(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    class Meta:
        ordering = ('last_name','first_name')
        def __str__(self):
            if self.died:
                return '{}, {} ({} - {})'.format(self.last_name,self.first_name,self.born)
    