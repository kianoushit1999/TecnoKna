from django.urls import path
from account.views import *
from TecnoKna import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('signin/', sign_in.as_view(), name='signin'),
                  path('signup/', sign_up.as_view(), name='signup'),
                  path('logout/', LogOut.as_view(), name='logout'),
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)