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
					Pembukuan_HajiForm,
					Pembukuan_Honor_KaryawanForm,

	)
from datetime import datetime

total_pengeluaran = 0
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

	total_pengeluaran = total


	context = {'obj':hasil,
				'total':total,
				'pengeluaran':pengeluaran,
	}
	return render(request,'pembukuan/tiket.html',context)


@login_required
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



	context = {'obj':'obj',
				'jemaah_haji':jemaah_haji,
				'jemaah_umroh':jemaah_umroh,
				'pemasukan_haji':total_pemasukan_haji,
				'pemasukan_umroh':total_pemasukan_umroh,
				'pengeluaran':total

				}
	return render(request,'pembukuan/index.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def tiket_arsip(request,month,year):
	pengeluaran = 'Tiket'
	query = request.GET.get("q", None)
	obj = Tiket.objects.all().order_by('-tanggal_input')

	objeks = Tiket.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = objeks.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def tiket_tambah(request,month,year):
	pengeluaran = 'Tiket'

	form = TiketForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/tiket/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def tiket_hapus(request,year,month,id = None):

	obj = get_object_or_404(Tiket,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/tiket/{year}/{month}/'.format(year = year,month=month))
#--------------LA---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def la_view(request,year,month):
	pengeluaran = 'LA'
	query = request.GET.get("q", None)
	obj = La.objects.all().order_by('-tanggal_input')
	objeks = La.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def la_tambah(request,year,month):
	pengeluaran = 'LA'

	form = LaForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/la/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def la_hapus(request,year,month,id=None):

	obj = get_object_or_404(La,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/la/{year}/{month}/'.format(year = year,month=month))		
#--------------Kendaraan---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def kendaraan(request,year,month,id = None):

	pengeluaran = 'Kendaraan'
	query = request.GET.get("q", None)
	obj = Kendaraan.objects.all().order_by('-tanggal_input')
	objeks = Kendaraan.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def kendaraan_tambah(request,year,month):
	pengeluaran = 'Kendaraan'

	form = KendaraanForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/kendaraan/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def kendaraan_hapus(request,year,month,id=None):
	obj = get_object_or_404(Kendaraan,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/kendaraan/{year}/{month}/'.format(year = year,month=month))		
#--------------pembukuan umroh---------------

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_umroh(request,year,month):

	pengeluaran = 'Pembukuan_Umroh'
	query = request.GET.get("q", None)
	obj = Pembukuan_Umroh.objects.all().order_by('-tanggal_input')
	objeks = Pembukuan_Umroh.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_umroh_tambah(request,year,month):
	pengeluaran = 'Pembukuan Umroh'

	form = Pembukuan_UmrohForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_umroh/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_umroh_hapus(request,year,month,id = None):
	obj = get_object_or_404(Pembukuan_Umroh,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_umroh/{year}/{month}/'.format(year = year,month=month))		
#--------------Handling---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def handling(request,year,month):

	pengeluaran = 'Handling'
	query = request.GET.get("q", None)
	obj = Handling.objects.all().order_by('-tanggal_input')
	objeks = Handling.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def handling_tambah(request,year,month):

	pengeluaran = 'Handling'

	form = HandlingForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/handling/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def handling_hapus(request,year,month,id = None):
	obj = get_object_or_404(Handling,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/handling/{year}/{month}/'.format(year = year,month=month))

#--------------paspor---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def paspor(request,year,month):

	pengeluaran = 'Paspor'
	query = request.GET.get("q", None)
	obj = Paspor.objects.all().order_by('-tanggal_input')
	objeks = Paspor.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def paspor_tambah(request,year,month):
	pengeluaran = 'Paspor'

	form = pasporForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/paspor/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def paspor_hapus(request,year,month,id = None):
	obj = get_object_or_404(Paspor,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/paspor/{year}/{month}/'.format(year = year,month=month))

#--------------LA---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def transfortasi(request,year,month):

	pengeluaran = 'Transportasi'
	query = request.GET.get("q", None)
	obj = Transportasiet.objects.all().order_by('-tanggal_input')
	objeks = Transfortasi.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def transfortasi_tambah(request,year,month):
	pengeluaran = 'Transportasi'

	form = TransfortasiForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/transportasi/{year}/{month}/'.format(year = year,month=month))		

			
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
def transfortasi_hapus(request,year,month,id = None):
	obj = get_object_or_404(Tiket,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/transportasi/{year}/{month}/'.format(year = year,month=month))
#--------------Pembukuan haji---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_haji(request,year,month):
	pengeluaran = 'Pembukuan_Haji'
	query = request.GET.get("q", None)
	obj = Pembukuan_Haji.objects.all().order_by('-tanggal_input')
	objeks = Pembukuan_Haji.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_haji_tambah(request,year,month):
	pengeluaran = 'Pembukuan Haji'

	form = Pembukuan_HajiForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_haji/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_haji_hapus(request,year,month,id = None):
	obj = get_object_or_404(Pembukuan_Haji,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_haji/{year}/{month}/'.format(year = year,month=month))
#--------------pembukuan pajak---------------

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_pajak(request,year,month):

	pengeluaran = 'Pembukuan Pajak'
	query = request.GET.get("q", None)
	obj = Pembukuan_Pajak.objects.all().order_by('-tanggal_input')
	objeks = Pembukuan_Pajak.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_pajak_tambah(request,year,month):
	pengeluaran = 'Pembukuan Pajak'

	form = Pembukuan_PajakForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_pajak/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_pajak_hapus(request,year,month,id = None):
	obj = get_object_or_404(Pembukuan_Pajak,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_pajak/')
#--------------Atk---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def atk(request,year,month):

	pengeluaran = 'ATK'
	query = request.GET.get("q", None)
	obj = ATK.objects.all().order_by('-tanggal_input')
	objeks = ATK.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def atk_tambah(request,year,month):
	pengeluaran = 'ATK'

	form = ATKForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/atk/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def atk_hapus(request,year,month,id = None):
	obj = get_object_or_404(ATK,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/atk/{year}/{month}/'.format(year = year,month=month))
#--------------Atk---------------
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_honor_karyawan(request,year,month):

	pengeluaran = 'Pembukuan Honor Karyawan'
	query = request.GET.get("q", None)
	obj = Pembukuan_Honor_Karyawan.objects.all().order_by('-tanggal_input')
	objeks = Pembukuan_Honor_Karyawan.objects.filter(tanggal_input__year=year,tanggal_input__month=month).order_by('-tanggal_input')
	b = 0
	for ob in objeks:
		b = b +ob.jumlah
	# print(b)
	total = b
	tanggal = datetime.now()
	bulan = tanggal.strftime("%B")
	tahun = tanggal.strftime('%Y')

	if query is not None:
		obj = obj.filter(
                Q(rincian__icontains=query)
                )
	context = {'obj':obj,
				'total':total,
				'pengeluaran':pengeluaran,
				'objeks':objeks,
				'bulan':bulan,
				'tahun':tahun,
	}
	return render(request,'pembukuan/tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_honor_karyawan_tambah(request,year,month):
	pengeluaran = 'Pembukuan Honor Karyawan'

	form = Pembukuan_Honor_KaryawanForm(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/dashboard/pembukuan_honor_karyawan/{year}/{month}/'.format(year = year,month=month))		

			
	context = {'form':form,'pengeluaran':pengeluaran}
	return render(request,'pembukuan/f-tiket.html',context)
@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pembukuan.com'))
def pembukuan_honor_karyawan_hapus(request,year,month,id = None):
	obj = get_object_or_404(Pembukuan_Honor_Karyawan,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/pembukuan_honor_karyawan/{year}/{month}/'.format(year = year,month=month))
