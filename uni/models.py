from django.db import models
#import datetime

# Create your models here.


class Fachbereich(models.Model):
    class Meta:
        verbose_name_plural= 'Fachbereiche'

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Studierende(models.Model):
    firstN = models.CharField(max_length=30)
    lastN = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.firstN} {self.lastN}'


class Lehrveranstaltung(models.Model):
    title = models.CharField(max_length=30)
    fachbereich = models.ForeignKey(Fachbereich, on_delete=models.SET_NULL, null=True)
    studierende = models.ManyToManyField(Studierende)
    #date = models.DateTimeField

    def __str__(self):
        s_string = ', '.join([f'{s.firstN} {s.lastN}' for s in self.studierende.all()])
        return f'{self.titel} ({s_string})'
