from django.db import models


RACES = [
        ('light', 'Peuple de la Lumière'),
        ('shadow', "Peuple de l'Ombre"),
        ('water', "Peuple de l'Eau"),
        ('fire', 'Peuple du Feu'),
        ('earth', 'Peuple de la Terre'),
        ('air', "Peuple de l'Air")
]


class Character(models.Model):
    name   = models.CharField(max_length = 32)
    player = models.CharField(max_length = 32)
    race   = models.CharField(max_length = 32, choices = RACES)
    level  = models.IntegerField()

    str = models.IntegerField()
    dex = models.IntegerField()
    agi = models.IntegerField()
    vig = models.IntegerField()
    vit = models.IntegerField()
    int = models.IntegerField()
    per = models.IntegerField()
    cha = models.IntegerField()
    wil = models.IntegerField()
    mem = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('view', args=[self.pk])
