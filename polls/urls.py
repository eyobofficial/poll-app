from django.urls import path
from . import views

# App namespace
app_name = 'polls'


# URL pattern rules
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='poll-detail'),
    path('<int:pk>/result/', views.result, name='poll-result'),
    path('<int:pk>/vote/', views.vote, name='vote'), 
]
