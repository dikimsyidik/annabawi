from django.shortcuts import render
from django.http import HttpResponse
from data_jemaah.models import Haji,Umroh
# Create your views here.
from django.template import Library
from data_jemaah.forms import Form_Input_Haji,Form_Input_Umroh
def get_class(value):
    return value.__class__.__name__
def index(request):

	haji = Haji.objects.all()
	umroh = Umroh.objects.all()

	for h in haji:
		print((h.__class__.__name__))
	context = {'haji':haji,
				'umroh':umroh,
	}
	template = 'annabawi/index.html'
	return render(request,template,context)




def daftar(request):
	jenis = 'Haji'
	form = Form_Input_Haji(request.POST or None)
	context = {'form':form,'jenis':jenis}
	template = 'annabawi/f-daftar.html'
	return render(request,template,context)

def daftar_umroh(request):
	jenis = 'Umroh'
	form = Form_Input_Umroh(request.POST or None)
	context = {'form':form,'jenis':jenis}

	template = 'annabawi/f-daftar.html'
	return render(request,template,context)
def terimakasih(request):
	jenis = 'Umroh'
	form = 'form'
	context = {'form':form}
	template = 'annabawi/makasih.html'
	return render(request,template,context)
