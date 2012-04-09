# Create your views here.
from models import Film, MokiAdmin, SimpleSite
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from datetime import datetime

def render_to_response(template_name, dictionary=None, context_instance=None, mimetype="text/html", request=None):
    from django.shortcuts import render_to_response
    global_dictionary = {"Filme":Film.objects, 'MokiAdmins':MokiAdmin.objects,
                         'SimpleSites':SimpleSite.objects.filter(enabled=True).filter(show_in_menu=True)}
    if dictionary is not None:
        global_dictionary.update(dictionary)
    if context_instance is not None:
        context = context_instance
    else:
        if request is not None:
            context = RequestContext(request)
        else:
            context = None
    return render_to_response(template_name, global_dictionary, context_instance=context, mimetype=mimetype)

def movie_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        #else:
    form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
