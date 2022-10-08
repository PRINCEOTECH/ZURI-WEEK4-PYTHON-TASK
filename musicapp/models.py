from django.db import models





class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=150)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.CharField(max_length=500)
    song_id = models.OneToOneField(Song, on_delete=models.CASCADE)

# Create your models here.
