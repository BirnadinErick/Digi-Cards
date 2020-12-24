from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
handler404 = 'home.views.view404'
# handler500 = 'my_app.views.server_error'

urlpatterns = [
                  path('guardian/', admin.site.urls),
                  path('', include('home.urls', namespace='home')),
                  path('digi-cards/', include('main.urls', namespace='main')),
                  path('digi-card-markdown/', include('markdownx.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
