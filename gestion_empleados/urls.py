from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', view=admin.site.urls),
    path('', include(('apps.departamento.urls', 'post'), namespace='post')),
    path('', include(('apps.persona.urls', 'users'), namespace='users'))

               ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)