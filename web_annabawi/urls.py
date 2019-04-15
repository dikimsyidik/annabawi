from django.urls import path
from.views import index,daftar,terimakasih,daftar_umroh
urlpatterns = [
    path('', index,name='index'),
    path('daftar_haji/', daftar,name='daftar_haji'),
    path('daftar_umroh', daftar_umroh,name='daftar_umroh'),
    path('asdawdaskudhawd/', terimakasih,name='makasih'),

     ]