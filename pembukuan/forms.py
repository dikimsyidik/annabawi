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

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}


class LaForm(forms.ModelForm):
		class Meta:
			model =La
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class KendaraanForm(forms.ModelForm):
		class Meta:
			model =Kendaraan
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class Pembukuan_UmrohForm(forms.ModelForm):
		class Meta:
			model =Tiket
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class HandlingForm(forms.ModelForm):
		class Meta:
			model =Handling
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class PasporForm(forms.ModelForm):
		class Meta:
			model =Paspor
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class TransfortasiForm(forms.ModelForm):
		class Meta:
			model =Transfortasi
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class ATKForm(forms.ModelForm):
		class Meta:
			model =ATK
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class Pembukuan_HajiForm(forms.ModelForm):
		class Meta:
			model =Pembukuan_Haji
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class Pembukuan_PajakForm(forms.ModelForm):
		class Meta:
			model =Pembukuan_Pajak
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

class Pembukuan_Honor_KaryawanForm(forms.ModelForm):
		class Meta:
			model =Pembukuan_Honor_Karyawan
			fields = [
				'rincian',
				'jumlah',

			] 
			

			widgets = {
				'rincian':forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder':'Rincian'}),
				'jumlah':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Jumlah'}),
			}

