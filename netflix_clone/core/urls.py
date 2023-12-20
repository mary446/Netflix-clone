from django.urls import path

from .views import add_to_list
urlpatterns = [
    path('add-to-list/', add_to_list, name='add-to-list'),
    path('', views.index, name ='index')
]