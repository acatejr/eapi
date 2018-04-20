from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='EAPI API')

urlpatterns = [
    path('', include('apphome.urls', namespace='home')),
    path('srer/', include('appsrer.urls', namespace='srer')),
    path('docs/', schema_view),
    path('admin/', admin.site.urls),
]
