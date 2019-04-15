from django.db import models
from uuid import uuid4

# Create your models here.
def create_id():
    return str(uuid4())[:5]

class Haji(models.Model):
	pemberangkatan = models.CharField(max_length=100)
	harga = models.IntegerField()
	timestamp       = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.pemberangkatan
	def get_cname(self):
		class_name = self.__class__.__name__
		return class_name 

class Umroh(models.Model):
	pemberangkatan = models.CharField(max_length=100)
	harga = models.IntegerField()
	timestamp       = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.pemberangkatan
	def get_cname(self):
		class_name = self.__class__.__name__
		return class_name 

def path_and_rename(instance, filename):
    return (str(instance)+".jpg")



class Jemaah_Hajis(models.Model):
	id = models.CharField(max_length=100,primary_key=True, default=create_id, editable=True)
	nama_lengkap = models.CharField(max_length=200)
	foto = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	rombongan = models.ForeignKey('Haji',on_delete=models.CASCADE,blank=True,null=True )
	alamat = models.TextField()
	no_ktp = models.IntegerField(blank=True,null=True)

	tempat_lahir = models.CharField(max_length=100,blank=True,null=True)
	tanggal_lahir  = models.CharField(max_length=100,blank=True,null=True)
	timestamp       = models.DateTimeField(auto_now_add=True)
	tunggakan = models.IntegerField(blank=True,null=True)
	no_hp = models.IntegerField()

	def save(self, *args, **kwargs):
		if not self.tunggakan:
			self.tunggakan = self.rombongan.harga
		super(Jemaah_Hajis, self).save(*args, **kwargs)

	def __str__(self):
		return self.nama_lengkap
class Pembayaran_Jemaah_Haji(models.Model):
	jemaah =  models.ForeignKey('Jemaah_Hajis',on_delete=models.CASCADE, blank=True,null=True)
	# judul_kegiatan =  models.CharField(max_length=100)
	# deskripsi =  models.TextField()
	jumlah = models.IntegerField(blank = True,null=True)
	waktu = models.DateField(auto_now_add=True)
	# nama = str(jemaah.nama_lengkap)


	def __str__(self):
		return self.jemaah.nama_lengkap
# ___________________________________END______________________________

#______________________________Umroh________________
class Jemaah_Umroh(models.Model):
	id = models.CharField(max_length=100,primary_key=True, default=create_id, editable=True)
	nama_lengkap = models.CharField(max_length=200)
	foto = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	no_ktp = models.IntegerField(blank=True,null=True)
	rombongan = models.ForeignKey('Umroh',on_delete=models.CASCADE,blank=True,null=True )
	alamat = models.TextField()
	tempat_lahir = models.CharField(max_length=100,blank=True,null=True)
	tanggal_lahir  = models.CharField(max_length=100,blank=True,null=True)
	timestamp       = models.DateTimeField(auto_now_add=True)
	tunggakan = models.IntegerField(blank=True,null=True)
	no_hp = models.IntegerField()

	def save(self, *args, **kwargs):
		if not self.tunggakan:
			self.tunggakan = self.rombongan.harga
		super(Jemaah_Umroh, self).save(*args, **kwargs)

	def __str__(self):
		return self.nama_lengkap

class Pembayaran_Jemaah_Umroh(models.Model):
	jemaah =  models.ForeignKey('Jemaah_Umroh',on_delete=models.CASCADE, blank=True,null=True)
	# judul_kegiatan =  models.CharField(max_length=100)
	# deskripsi =  models.TextField()
	jumlah = models.IntegerField(blank = True,null=True)
	waktu = models.DateField(auto_now_add=True)
	# nama = str(jemaah.nama_lengkap)


	def __str__(self):
		return self.jemaah.nama_lengkap




