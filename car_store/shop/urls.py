from django.urls import path, include
from .views import *

urlpatterns = [
    path('', CarViewSet.as_view({'get': 'list', 'post': 'create'}),
                                  name='title_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                          'delete': 'destroy'}),name='title_detail'),


    path('model', ModelViewSet.as_view({'get': 'list', 'post': 'create'}),
                                         name='model_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve', 'put': 'update'
                                                     ,'delete': 'destroy'}), name='model_detail'),


    path('marka', MarkaViewSet.as_view({'get': 'list',
                                       'post': 'create'}),
                                         name='marka_list'),
    path('marka/<int:pk>/', MarkaViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='marka_detail')
]