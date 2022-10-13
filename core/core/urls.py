from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('cursos/', include('cursos.urls')),
    path('contato/', include('contato.urls')),
    path('contas/', include('autenticacao.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('criar_conta/', include('contas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
