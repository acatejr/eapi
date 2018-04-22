from django.urls import path
from .views import HomeView

app_name = 'apphome'

urlpatterns = [
    path(r'', HomeView.as_view(), name='home'),
]