from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

handler400 = 'home.views.view400'
handler403 = 'home.views.view403'
handler404 = 'home.views.view404'
handler500 = 'home.views.view500'

urlpatterns = [
                  path('guardian/', admin.site.urls),
                  path('', include('home.urls', namespace='home')),
                  path('digi-cards/', include('main.urls', namespace='main')),
                  path('digi-card-markdown/', include('markdownx.urls')),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from home.views import view400, view403, view404, view500

    urlpatterns += [
        path('500', view500),
        path('404', view404),
        path('403', view403),
        path('400', view400),
    ]
