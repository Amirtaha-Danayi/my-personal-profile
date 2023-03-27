from django.urls import path
from . import views

urlpatterns = [
    path('', views.Show_index.as_view(), name='show_index')
]