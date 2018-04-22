from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='EAPI')

urlpatterns = [
    path('', include('apphome.urls', namespace='home')),
    path('srer/', include('appsrer.urls', namespace='srer')),
    path('wgew/', include('appwgew.urls', namespace='wgew')),
    path('apidocs/', schema_view, name='apidocs'),
    path('admin/', admin.site.urls),
]
