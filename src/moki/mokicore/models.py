from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from datetime import datetime
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class FilmManager(models.Manager):
    use_for_related_fields = True
    def current_semester(self):
        return self.filter(date__gt=datetime(2011,10,1))\
                   .filter(date__lt=datetime(2012,3,1))
class Film(models.Model):
    titel = models.CharField(max_length=200)
    thema = models.CharField(max_length=50, null=True, blank=True)
    aktions_titel = models.CharField(max_length=50, null=True, blank=True)
    aktions_beschreibung = models.TextField(null=True, blank=True)
    imdb_id = models.CharField(max_length=50)
    cover = ImageField(upload_to='movie/cover')
    description = models.TextField()
    date = models.DateField()

    objects = FilmManager()
    def __unicode__(self):
        return u"Film(%s) - %s" % (self.pk, self.titel)

    def url_titel(self):
        return slugify(self.titel)

    def url(self):
        return reverse("mokicore.views.film", 
                       kwargs={"film_id": self.pk,
                               "site": self.url_titel})
class MokiAdmin(models.Model):
    user = models.OneToOneField(User)
    bild = ImageField(upload_to='user/face', null=True)

    def __unicode__(self):
        return u"MokiAdmin(%s) - %s" % (self.pk, self.name)

class SimpleSite(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    enabled = models.BooleanField(default=False)
    show_in_menu = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

