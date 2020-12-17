from django.urls import path

from account.views import sign_up, sign_in
from blog.views import *
from django.conf.urls.static import static

urlpatterns = [
                  path('signin/', sign_in, name='signin'),
                  path('sign_up/', sign_up, name='signup'),
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)