from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from data_jemaah.models import Jemaah_Hajis,Jemaah_Umroh,Pembayaran_Jemaah_Umroh,Pembayaran_Jemaah_Haji
from django.http import HttpResponseRedirect,HttpResponse
from .models import (
					Tiket,
					La,
					Kendaraan,
					Pembukuan_Umroh,
					Handling,
					Paspor,
					Transfortasi,
					ATK,
					Pembukuan_Haji,
					Pembukuan_Pajak,
					Pembukuan_Honor_Karyawan,
					)
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test
from itertools import chain
from .forms import (TiketForm,
					LaForm,
					KendaraanForm,
					Pembukuan_UmrohForm,
					HandlingForm,
					PasporForm,
					TransfortasiForm,
					ATKForm,
					Pembukuan_PajakForm,
					Pembukuan_Honor_KaryawanForm,

	)
def rekap(request):
	pengeluaran = 'Rekapan Keseluruhan'
	query = request.GET.get("q", None)
	obj = Tiket.objects.all()
	tiket = Tiket.objects.all()
	la = La.objects.all()
	kendaraan = Kendaraan.objects.all()
	pembukuan_umroh = Pembukuan_Umroh.objects.all()
	handling = Handling.objects.all()
	paspor = Paspor.objects.all()
	transportasi = Transfortasi.objects.all()
	atk = ATK.objects.all()
	pembukuan_haji = Pembukuan_Haji.objects.all()
	pembukuan_pajak = Pembukuan_Pajak.objects.all()
	pembukuan_honor = Pembukuan_Honor_Karyawan.objects.all()
	gabung = sorted(chain(tiket,
						la,
						kendaraan,
						pembukuan_umroh,
						handling,
						paspor,
						transportasi,
						atk,
						pembukuan_haji,
						pembukuan_pajak,
						pembukuan_honor,
						),key = lambda instance:instance.jumlah)
	hasil = gabung

	total = 0
	for gab in hasil:
		total = total +gab.jumlah
		print(gab.jumlah)
	print(total)



	context = {'obj':hasil,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)


@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def dashboard(request):
	jemaah_haji = Jemaah_Hajis.objects.all().count()
	jemaah_umroh = Jemaah_Umroh.objects.all().count()
	pemasukan_haji = Pembayaran_Jemaah_Haji.objects.all()
	pemasukan_umroh = Pembayaran_Jemaah_Umroh.objects.all()
	total_pemasukan_umroh = 0
	total_pemasukan_haji = 0
	for pem_umroh in pemasukan_umroh:
		total_pemasukan_umroh = total_pemasukan_umroh + pem_umroh.jumlah


	for pem_haji in pemasukan_haji:
		total_pemasukan_haji = total_pemasukan_haji + pem_haji.jumlah


	context = {'obj':'obj',
				'jemaah_haji':jemaah_haji,
				'jemaah_umroh':jemaah_umroh,
				'pemasukan_haji':total_pemasukan_haji,
				'pemasukan_umroh':total_pemasukan_umroh,

				}
	return render(request,'pembukuan/index.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def tiket(request):
	pengeluaran = 'Tiket'
	query = request.GET.get("q", None)
	obj = Tiket.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def tiket_tambah(request):
	pengeluaran = 'Tiket'

	form = TiketForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/tiket/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def tiket_hapus(request,id = None):

	obj = get_object_or_404(Tiket,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/tiket/')
#--------------LA---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def la_view(request):
	pengeluaran = 'LA'
	query = request.GET.get("q", None)
	obj = La.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def la_tambah(request):
	pengeluaran = 'LA'

	form = LaForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/la/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def la_hapus(request):

	obj = get_object_or_404(La,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/la/')
#--------------Kendaraan---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def kendaraan(request):

	pengeluaran = 'Kendaraan'
	query = request.GET.get("q", None)
	obj = Kendaraan.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def kendaraan_tambah(request):
	pengeluaran = 'Kendaraan'

	form = KendaraanForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/kendaraan/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def kendaraan_hapus(request,id=None):
	obj = get_object_or_404(Kendaraan,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/kendaraan/')
#--------------pembukuan umroh---------------

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_umroh(request):

	pengeluaran = 'Pembukuan_Umroh'
	query = request.GET.get("q", None)
	obj = Pembukuan_Umroh.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_umroh_tambah(request):
	pengeluaran = 'Pembukuan Umroh'

	form = Pembukuan_UmrohForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_umroh/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))	
def pembukuan_umroh_edit(request):

	obj = Tiket.objects.all()
	# context = {'obj':obj}
	return render(request,'pembukuan/index.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_umroh_hapus(request,id = None):
	obj = get_object_or_404(Pembukuan_Umroh,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_umroh/')
#--------------Handling---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def handling(request):

	pengeluaran = 'Handling'
	query = request.GET.get("q", None)
	obj = Handling.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def handling_tambah(request):

	pengeluaran = 'Handling'

	form = HandlingForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/handling/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def handling_hapus(request,id = None):
	obj = get_object_or_404(Handling,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/handling/')

#--------------paspor---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def paspor(request):

	pengeluaran = 'Paspor'
	query = request.GET.get("q", None)
	obj = Paspor.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def paspor_tambah(request):
	pengeluaran = 'Paspor'

	form = pasporForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/paspor/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def paspor_hapus(request,id = None):
	obj = get_object_or_404(Paspor,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/paspor/')

#--------------LA---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def transfortasi(request):

	pengeluaran = 'Transportasi'
	query = request.GET.get("q", None)
	obj = Transportasiet.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def transfortasi_tambah(request):
	pengeluaran = 'Transportasi'

	form = TransfortasiForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/transportasi/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def transfortasi_edit(request):

	obj = Tiket.objects.all()
	context = {'obj':obj}
	return render(request,'pembukuan/index.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def transfortasi_hapus(request,id = None):
	obj = get_object_or_404(Tiket,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/transportasi/')
#--------------Pembukuan haji---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_haji(request):
	pengeluaran = 'Pembukuan_Haji'
	query = request.GET.get("q", None)
	obj = Pembukuan_Haji.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_haji_tambah(request):
	pengeluaran = 'Pembukuan Haji'

	form = Pembukuan_HajiForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_haji/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_haji_hapus(request,id = None):
	obj = get_object_or_404(Pembukuan_Haji,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_haji/')
#--------------pembukuan pajak---------------

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_pajak(request):

	pengeluaran = 'Pembukuan Pajak'
	query = request.GET.get("q", None)
	obj = Pembukuan_Pajak.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_pajak_tambah(request):
	pengeluaran = 'Pembukuan Pajak'

	form = Pembukuan_PajakForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_pajak/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_pajak_hapus(request,id = None):
	obj = get_object_or_404(Pembukuan_Pajak,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_pajak/')
#--------------Atk---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def atk(request):

	pengeluaran = 'ATK'
	query = request.GET.get("q", None)
	obj = ATK.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def atk_tambah(request):
	pengeluaran = 'ATK'

	form = ATKForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/atk/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def atk_hapus(request,id = None):
	obj = get_object_or_404(ATK,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/atk/')
#--------------Atk---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_honor_karyawan(request):

	pengeluaran = 'Pembukuan Honor Karyawan'
	query = request.GET.get("q", None)
	obj = Pembukuan_Honor_Karyawan.objects.all().order_by('-tanggal_input')
	b = 0
	
	for ob in obj:
		b = b +ob.jumlah
	print(b)
	total = b

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_honor_karyawan_tambah(request):
	pengeluaran = 'Pembukuan Honor Karyawan'

	form = Pembukuan_Honor_KaryawanForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_honor_karyawan/')		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_honor_karyawan_hapus(request):
	obj = get_object_or_404(Pembukuan_Honor_Karyawan,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_honor_karyawan/')
