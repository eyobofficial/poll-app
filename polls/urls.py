from django.urls import path
from . import views

# App namespace
app_name = 'polls'


# URL pattern rules
urlpatterns = [
   path('', views.index, name='index'),
]