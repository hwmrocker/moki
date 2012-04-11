# Create your views here.
from models import Film, MokiAdmin, SimpleSite
from views import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from datetime import datetime
import imdb
import urllib2
from urlparse import urlparse
from django.core.files import File

import logging
logger = logging.getLogger('custom')
dbg = logger.debug

from django import forms

class UploadFileForm(forms.Form):
    file  = forms.FileField()


def movie_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        #else:
    form = UploadFileForm()
    return render_to_response('upload.html', {'form': form}, request=request)

def handle_uploaded_file(fileh):
    q = imdb.IMDb()
    dbg(len(fileh))
    for line in fileh.readlines():
        mid, date, thema, aktion = line.split('|')
        m = q.get_movie(mid)
        newf = Film()
        newf.titel = m['title']
        newf.thema = thema
        newf.aktions_titel = aktion
        newf.imdb_id = mid
        newf.description = ''
        newf.date = datetime.strptime(date,'%d.%m.%Y')
        cover_url = m.get('full-size cover url')
        if cover_url:
            newf.cover.save(date+'.jpg',
                            File(urllib2.urlopen(cover_url).read()),
                            save=True)
        newf.save()
