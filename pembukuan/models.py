from django.db import models

# Create your models here.


class Tiket(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
class La(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
class Kendaraan(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
class Pembukuan_Umroh(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian

class Handling(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian

class Paspor(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
class Transfortasi(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian

class ATK(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
class Pembukuan_Haji(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
class Pembukuan_Pajak(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
class Pembukuan_Honor_Karyawan(models.Model):
	rincian = models.CharField(max_length=200)
	tanggal_input       = models.DateTimeField(auto_now_add=False)
	jumlah = models.IntegerField()

	def __str__(self):
		return self.rincian
		
