from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blackdog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.indexView'),
	url(r'^login/$', 'autenticacion.views.loginView'),
	url(r'^login/create/user$', 'usuario.views.createUser'),      
	url(r'^login/error/$', 'autenticacion.views.errorview'),  
	url(r'^autenticacion/valida/$', 'autenticacion.views.sucessfullview'),

    #url referido
    url(r'^referido/referir/$', 'referido.views.referirForm'),
    url(r'^referido/enviar/invitacion$', 'referido.views.enviarInvitacion'),

    url(r'^admin/', include(admin.site.urls)),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)