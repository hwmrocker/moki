from django.conf.urls.defaults import *

urlpatterns = patterns('mokicore.admin_views',
    (r'filmupload', 'movie_upload'),
)
urlpatterns += patterns('mokicore.views',
    (r'^$', 'index'),
    (r'^filme', 'filme'),
    (r'^film/(?P<film_id>[0-9]+)/(?P<site>[\w]*)', 'film'),
    (r'^(?P<name>[\w]+)', 'dispatch'),
)

