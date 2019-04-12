from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse

from .models import Jemaah_Hajis,Haji,Umroh,Pembayaran_Jemaah_Haji,Pembayaran_Jemaah_Umroh,Jemaah_Umroh
from django.db.models import Q

from .forms import PembayaranForm,TambahJadwal_Haji,TambahJadwal_Umroh,PembayaranFormUmroh,Form_Input_Haji,Form_Input_Haji_Edit
# Create your views here.
from .forms import Form_Input_Haji_Edit,Form_Input_Umroh
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def tambah_haji(request):
	jenis = 'Haji'

	form = TambahJadwal_Haji(request.POST or None)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()

		
		return HttpResponseRedirect('/dashboard/jadwal_pemberangkatan_haji/')		

			
	context = {'form':form,'jenis':jenis}
	return render(request,'pembukuan/f-pemberangkatan-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))	
def tambah_umroh(request):
	form = TambahJadwal_Umroh(request.POST or None)	
	jenis = 'Umroh'
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()

		
		return HttpResponseRedirect('/dashboard/jadwal_pemberangkatan_umroh/')		

			
	context = {'form':form,'jenis':jenis}
	return render(request,'pembukuan/f-pemberangkatan-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))	
def list_haji(request):
	obj = Haji.objects.all().order_by('-timestamp')
	jenis = 'Haji'
	query = request.GET.get("q", None)
	if query is not None:
		obj = obj.filter(
                Q(pemberangkatan__icontains=query)
                )
	context = {'obj':obj,'jenis':jenis}
	return render(request,'pembukuan/pemberangkatan-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))	
def detail_haji(request,id = None):
	obj = get_object_or_404(Haji,id = id)
	jemaah = obj.jemaah_hajis_set.all()
	jenis = 'Haji'
	query = request.GET.get("q", None)
	if query is not None:
		jemaah = jemaah.filter(
                Q(nama_lengkap__icontains=query)
                )

	
	context = {'obj':obj,'jemaah':jemaah,'jenis':jenis}
	return render(request,'pembukuan/list-jemaah-pemberangkatan-haji.html',context)
	

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def list_umroh(request):
	obj = Umroh.objects.all().order_by('-timestamp')
	jenis = 'Umroh'
	query = request.GET.get("q", None)
	if query is not None:
		obj = obj.filter(
                Q(pemberangkatan__icontains=query)
                )
	context = {'obj':obj,'jenis':jenis}
	return render(request,'pembukuan/pemberangkatan-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))	
def detail_umroh(request, id=None):
	obj = get_object_or_404(Umroh,id = id)
	jemaah = obj.jemaah_umroh_set.all()
	jenis = 'Umroh'
	query = request.GET.get("q", None)
	if query is not None:
		jemaah = jemaah.filter(
                Q(nama_lengkap__icontains=query)
                )

	
	context = {'obj':obj,'jemaah':jemaah,'jenis':jenis}
	return render(request,'pembukuan/list-jemaah-pemberangkatan-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))	
def edit_haji(request,id = None):
	jenis = 'Haji'
	objek = get_object_or_404(Haji,id = id)

	form = TambahJadwal_Haji(request.POST or None,instance=objek)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()

		
		return HttpResponseRedirect('/dashboard/jadwal_pemberangkatan_haji/')		

			
	context = {'form':form,'jenis':jenis}
	return render(request,'pembukuan/f-pemberangkatan-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def edit_umroh(request,id = None):
	jenis = 'Umroh'
	objek = get_object_or_404(Umroh,id = id)

	form = TambahJadwal_Umroh(request.POST or None,instance=objek)	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		obj.save()

		
		return HttpResponseRedirect('/dashboard/jadwal_pemberangkatan_umroh/')		

			
	context = {'form':form,'jenis':jenis}
	return render(request,'pembukuan/f-pemberangkatan-haji.html',context)
def hapus_haji(request,id = None):
	objek = get_object_or_404(Haji,id = id)
	objek.delete()
	return HttpResponseRedirect('/dashboard/jadwal_pemberangkatan_haji/')

def hapus_umroh(request,id = None):
	objek = get_object_or_404(Umroh,id = id)
	objek.delete()

	return HttpResponseRedirect('/dashboard/jadwal_pemberangkatan_umroh/')

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_haji(request):
	jenis = 'Haji'
	obj = Jemaah_Hajis.objects.all().order_by('-timestamp')
	query = request.GET.get("q", None)
	if query is not None:
		obj = obj.filter(
                Q(nama_lengkap__icontains=query)
                )

	context = {'obj':obj,'jenis':jenis}
	return render(request,'pembukuan/list-jemaah-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_haji_detail(request,id = None):
	obj = get_object_or_404(Jemaah_Hajis,id = id)
	jenis = 'Haji'
	riwayat_pembayaran = obj.pembayaran_jemaah_haji_set.all()
	total = 0
	for riw in riwayat_pembayaran:
		total = total+riw.jumlah
	context = {'obj':obj,'jenis':jenis,'pembayaran':riwayat_pembayaran,'total':total}
	return render(request,'pembukuan/detail-jamaah.html',context)


@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_haji_tambah(request):
	form = Form_Input_Haji(request.POST,request.FILES or None)
	context = {'form':form}
	jenis = 'Haji'
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		
		obj.save()

		
		return HttpResponseRedirect('/dashboard/list_jemaah_haji/')		


	return render(request,'pembukuan/f-input-jemaah.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_haji_edit(request,id = None):
	objek = get_object_or_404(Jemaah_Hajis,id = id)
	form = Form_Input_Haji_Edit(request.POST or None,instance=objek)
	jenis = 'Haji'

	if form.is_valid():
		form = Form_Input_Haji_Edit(request.POST,request.FILES or None,instance=objek)
	
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		
		obj.save()

		
		return HttpResponseRedirect('/dashboard/list_jemaah_haji/')		

	context = {'form':form}

	return render(request,'pembukuan/f-input-jemaah.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_haji_hapus(request,id = None):
	obj = get_object_or_404(Jemaah_Hajis,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/list_jemaah_haji/')		




@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_umroh(request):
	jenis = 'Umroh'
	obj = Jemaah_Umroh.objects.all().order_by('-timestamp')
	query = request.GET.get("q", None)
	if query is not None:
		obj = obj.filter(
                Q(nama_lengkap__icontains=query)
                )

	context = {'obj':obj,'jenis':jenis}
	return render(request,'pembukuan/list-jemaah-haji.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_umroh_detail(request,id = None):
	obj = get_object_or_404(Jemaah_Umroh,id = id)
	jenis = 'Umroh'
	riwayat_pembayaran = obj.pembayaran_jemaah_umroh_set.all()
	total = 0
	for riw in riwayat_pembayaran:
		total = total+riw.jumlah
	context = {'obj':obj,'jenis':jenis,'pembayaran':riwayat_pembayaran,'total':total}
	return render(request,'pembukuan/detail-jamaah.html',context)


@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_umroh_tambah(request):
	form = Form_Input_Umroh(request.POST,request.FILES or None)
	context = {'form':form}
	jenis = 'Umroh'
	if form.is_valid():
		obj  = form.save(commit=False)
		
		obj.save()

		
		return HttpResponseRedirect('/dashboard/list_jemaah_umroh/{}'.format(obj.id))		


	return render(request,'pembukuan/f-input-jemaah.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_umroh_edit(request):
	objek = get_object_or_404(Jemaah_Umroh,id = id)
	form = Form_Input_Umroh_Edit(request.POST or None,instance=objek)
	jenis = 'Umroh'

	if form.is_valid():
		form = Form_Input_Umroh_Edit(request.POST,request.FILES or None,instance=objek)
	
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		
		obj.save()

		
		return HttpResponseRedirect('/dashboard/list_jemaah_umroh/{}'.format(objek.id))		

	context = {'form':form}

	return render(request,'pembukuan/f-input-jemaah.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def jemaah_umroh_hapus(request,id = None):
	obj = get_object_or_404(Jemaah_Umroh,id = id)
	obj.delete()
	return HttpResponseRedirect('/dashboard/list_jemaah_umroh/')		


@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def pembayaran_haji(request):	# jemaah = get_object_or_404(Jemaah_Hajis,id = id)
	form = PembayaranForm(request.POST or None)
	jenis = 'Haji'
	
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		
		obj.save()
		return HttpResponseRedirect("/dashboard/pembayaran_haji/kwitansi_haji/{num}".format(num=obj.id))

			
	context = {'form':form,'jenis':jenis}
	return render(request,'pembukuan/pembayaran.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def pembayaran_umroh(request):
	form = PembayaranFormUmroh(request.POST or None)
	jenis = 'Umroh'
	if form.is_valid():
		# hasil = int(form.data['tunggakan'])- int(form.data['bayar'])
		obj  = form.save(commit=False)
		
		obj.save()

		
		return HttpResponseRedirect('/dashboard/pemasukan_umroh/hasil/')		

			
	context = {'form':form,'jenis':jenis}
	return render(request,'pembukuan/pembayaran.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def pemasukan_haji(request):
	obj = Pembayaran_Jemaah_Haji.objects.all().order_by('-waktu')
	jenis = 'Haji'
	total = 0
	for tot in obj :
		total = total + tot.jumlah
	context = {'obj':obj,'jenis':jenis,'total':total}
	return render(request,'pembukuan/pemasukan.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def pemasukan_umroh(request):
	obj = Pembayaran_Jemaah_Umroh.objects.all().order_by('-waktu')
	jenis = 'Umroh'
	total = 0
	for tot in obj :
		total = total + tot.jumlah
	context = {'obj':obj,'jenis':jenis,'total':total}
	return render(request,'pembukuan/pemasukan.html',context)

@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@admin.com'))
def kwitansi_haji(request,id = None):
	obj = get_object_or_404(Pembayaran_Jemaah_Haji,id = id)
	jenis = 'Haji'
	query = request.GET.get("q", None)


	
	context = {'obj':obj,'jenis':jenis }
	return render(request,'pembukuan/kwitansi.html',context)
