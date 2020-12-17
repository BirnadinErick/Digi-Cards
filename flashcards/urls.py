from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('guardian/', admin.site.urls),
                  path('', include('home.urls', namespace='home')),
                  path('digi-cards/', include('main.urls', namespace='main')),
                  path('digi-card-markdown/', include('markdownx.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
