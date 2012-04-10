# Create your views here.
from models import Film, MokiAdmin, SimpleSite
from views import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from datetime import datetime

import logging
logger = logging.getLogger('custom')
dbg = logger.debug

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()


def movie_upload(request):
    dbg(request)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        #else:
    form = UploadFileForm()
    return render_to_response('upload.html', {'form': form}, request=request)

def handle_uploaded_file(fileh):
    dbg(len(fileh))
    for line in fileh.readlines():
        dbg(line)
