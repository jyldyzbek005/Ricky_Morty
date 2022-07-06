from django.db import models


class Location(models.Model):
    location_list = models.CharField(max_length=2333, verbose_name='локация листа')
    planet = models.CharField(max_length=344,verbose_name='месео проживание')
    dimension = models.CharField(verbose_name='измерение',max_length=344)

    def __str__(self) -> str:
        return self.location_list

class Character(models.Model):
    title = models.CharField(max_length=236, verbose_name='зоголовок')
    image = models.ImageField(verbose_name='изображение')
    character = models.CharField(max_length=255, verbose_name='имя персонажа')

    def __str__(self) -> str:
        return self.title

class Epizode(models.Model):
    seria = models.CharField(max_length=400,verbose_name='серия')
    desc = models.CharField(max_length=400,verbose_name='описания')

    def __str__(self) -> str:
        return self.seria

    class Meta:
        verbose_name = ''
    
        


