from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('tasklist/',tasklist,name='tasklist'),
    path('update/<id>',update,name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('taskcreation/',taskcreation,name='taskcreation')
]
