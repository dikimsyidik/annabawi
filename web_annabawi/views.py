from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context = {}
	template = 'annabawi/index.html'
	return render(request,template,context)




def daftar(request):
	jenis = 'Umroh'
	form = 'form'
	context = {'form':form,'jenis':jenis}
	template = 'annabawi/f-daftar.html'
	return render(request,template,context)

def daftar_umroh(request):
	jenis = 'Umroh'
	form = 'form'
	context = {'form':form}
	template = 'annabawi/f-daftar.html'
	return render(request,template,context)
def terimakasih(request):
	jenis = 'Umroh'
	form = 'form'
	context = {'form':form}
	template = 'annabawi/makasih.html'
	return render(request,template,context)
