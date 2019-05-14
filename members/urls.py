from django.urls import path

from . import views

app_name = 'members'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index')
        path('<char:full_name>/', views.PersonView.as_view(), name='person'),
        ]
