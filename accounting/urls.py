from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^accounting/$', views.xlsx_upload_accounting, name='statements'),
    url(r'^ledger/$', views.General_Ledger, name='GL'),
    url(r'^modelos/$', views.download, name='modelo'),#esta é apenas a interface para o download
    url(r'^download/$', views.excel_download, name='excel'),# isto realiza o download

]
