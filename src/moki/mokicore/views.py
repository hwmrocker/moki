# Create your views here.
from models import Film, MokiAdmin, SimpleSite
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from datetime import datetime
from django.core.context_processors import csrf

import logging
logger = logging.getLogger('custom')
dbg = logger.debug


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

    context.update(csrf(request))
    return render_to_response(template_name, global_dictionary, context_instance=context, mimetype=mimetype)

def index(request):
    next_movie = Film.objects.filter(date__gte=datetime.now())[0:1] or None
    if next_movie:
        next_movie = next_movie[0]
    home_site = SimpleSite.objects.filter(name='home')[0] or None
    return render_to_response("index.html", {'next_movie':next_movie,
                                             'site_obj':home_site}, request=request)

def dispatch(request, name):
    if name in globals():
        return globals()[name](request)
    else:
        return default(request, name)

def film(request, film_id=None, site=None):
    film = get_object_or_404(Film, pk=film_id)
    return render_to_response("film.html", {"film":film}, request=request)

def filme(request):
    return render_to_response("filme.html", request=request)

def team(request, site):
    return render_to_response("team.html", request=request)

def default(request, name, extras=""):
    simple_site = get_object_or_404(SimpleSite, name=name)
    return render_to_response("default.html", {'site_obj': simple_site}, request=request)

#def impressum(request):
#    return render_to_response("impressum.html")
#
#def anfahrt(request, site):
#    return render_to_response("anfahrt.html", request=request)
