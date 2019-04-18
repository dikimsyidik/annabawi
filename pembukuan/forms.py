from django import forms
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
class TiketForm(forms.ModelForm):
		class Meta:
			model =Tiket
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}


class LaForm(forms.ModelForm):
		class Meta:
			model =La
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class KendaraanForm(forms.ModelForm):
		class Meta:
			model =Kendaraan
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class Pembukuan_UmrohForm(forms.ModelForm):
		class Meta:
			model =Tiket
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class HandlingForm(forms.ModelForm):
		class Meta:
			model =Handling
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class PasporForm(forms.ModelForm):
		class Meta:
			model =Paspor
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class TransfortasiForm(forms.ModelForm):
		class Meta:
			model =Transfortasi
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class ATKForm(forms.ModelForm):
		class Meta:
			model =ATK
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class Pembukuan_HajiForm(forms.ModelForm):
		class Meta:
			model =Pembukuan_Haji
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class Pembukuan_PajakForm(forms.ModelForm):
		class Meta:
			model =Pembukuan_Pajak
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}

class Pembukuan_Honor_KaryawanForm(forms.ModelForm):
		class Meta:
			model =Pembukuan_Honor_Karyawan
			fields = [
				'rincian',
				'jumlah',
				'tanggal_input',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
				'tanggal_input':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tanggal'}),

			}
