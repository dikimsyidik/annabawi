from django import forms

from .models import Pembayaran_Jemaah_Haji,Haji,Umroh,Pembayaran_Jemaah_Umroh,Jemaah_Hajis,Jemaah_Umroh

class TambahJadwal_Haji(forms.ModelForm):
	class Meta:
		model = Haji
		fields = [
			'pemberangkatan',
			'harga',

			


		]
		widgets = {
			'pemberangkatan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Jadwal'}),
			'harga':forms.NumberInput(attrs={'class': 'form-control','value':'','placeholder':'Harga'}),

		}

class TambahJadwal_Umroh(forms.ModelForm):
	class Meta:
		model = Umroh
		fields = [
			'pemberangkatan',
			'harga',

		]
		widgets = {
			'pemberangkatan':forms.TextInput(attrs={'class':'form-control',"placeholder":"Jadwal"}),
			'harga':forms.TextInput(attrs={"class":"form-control" ,"placeholder":"Harga", "aria-label":"Harga"}),
		}
class PembayaranForm(forms.ModelForm):
	class Meta:
		model = Pembayaran_Jemaah_Haji
		fields = [
			'jemaah',
			'jumlah',

			


		]
		widgets = {

			'jemaah':forms.TextInput(attrs={'class': 'form-control','placeholder':'ID Jemaah'}),
			'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),

		}
class PembayaranFormUmroh(forms.ModelForm):
	class Meta:
		model = Pembayaran_Jemaah_Umroh
		fields = [
			'jemaah',
			'jumlah',

			


		]
		widgets = {
			'jemaah':forms.TextInput(attrs={'class': 'form-control','placeholder':'ID Jemaah'}),
			'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),

		}
class Form_Input_Haji(forms.ModelForm):
	class Meta:
		model = Jemaah_Hajis
		fields = [

			'nama_lengkap',
			'foto',
			'no_ktp',
			'rombongan',
			'alamat',
			# 'tempat_lahir',
			# 'tanggal_lahir',
			'no_hp',


			


		]
		widgets = {
			'nama_lengkap':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_ktp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. KTP'}),
			'rombongan':forms.Select(attrs={'class': 'form-control','placeholder':''}),
			'alamat':forms.Textarea(attrs={'class': 'form-control','rows':3,'placeholder':'Alamat'}),
			'no_hp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. Telepon'}),
			'foto':forms.FileInput(attrs={'class': 'dropify','placeholder':''}),
		}


class Form_Input_Haji_Edit(forms.ModelForm):
	
	class Meta:
		model = Jemaah_Hajis
		fields = [

			'nama_lengkap',
			'foto',
			'no_ktp',
			'rombongan',
			'alamat',
			# 'tempat_lahir',
			# 'tanggal_lahir',
			'no_hp',


			


		]
		kiri = '{{'
		kanan = '}}'
		widgets = {
			'nama_lengkap':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_ktp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. KTP'}),
			'rombongan':forms.Select(attrs={'class': 'form-control','placeholder':''}),
			'alamat':forms.Textarea(attrs={'class': 'form-control','rows':3,'placeholder':'Alamat'}),
			'no_hp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. Telepon'}),
			'foto':forms.FileInput(attrs={'class': 'dropify'}),
		}


class Form_Input_Umroh(forms.ModelForm):
	class Meta:
		model = Jemaah_Umroh
		fields = [

			'nama_lengkap',
			'foto',
			'no_ktp',
			'rombongan',
			'alamat',
			# 'tempat_lahir',
			# 'tanggal_lahir',
			'no_hp',


			


		]
		widgets = {
			'nama_lengkap':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_ktp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. KTP'}),
			'rombongan':forms.Select(attrs={'class': 'form-control','placeholder':''}),
			'alamat':forms.Textarea(attrs={'class': 'form-control','rows':3,'placeholder':'Alamat'}),
			'no_hp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. Telepon'}),
			'foto':forms.FileInput(attrs={'class': 'dropify','placeholder':''}),
		}


class Form_Input_Umroh_Edit(forms.ModelForm):
	
	class Meta:
		model = Jemaah_Umroh
		fields = [

			'nama_lengkap',
			'foto',
			'no_ktp',
			'rombongan',
			'alamat',
			# 'tempat_lahir',
			# 'tanggal_lahir',
			'no_hp',


			


		]
		kiri = '{{'
		kanan = '}}'
		widgets = {
			'nama_lengkap':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_ktp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. KTP'}),
			'rombongan':forms.Select(attrs={'class': 'form-control','placeholder':''}),
			'alamat':forms.Textarea(attrs={'class': 'form-control','rows':3,'placeholder':'Alamat'}),
			'no_hp':forms.NumberInput(attrs={'class': 'form-control','placeholder':'No. Telepon'}),
			'foto':forms.FileInput(attrs={'class': 'dropify'}),
		}


