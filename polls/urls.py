from django.urls import path
from . import views

# App namespace
app_name = 'polls'


# URL pattern rules
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.QuestionDetail.as_view(), name='poll-detail'),
    path('<int:pk>/result/', views.result, name='poll-result'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]
