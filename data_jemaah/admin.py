from django.contrib import admin
from .models import Haji,Jemaah_Hajis,Pembayaran_Jemaah_Haji,Umroh,Jemaah_Umroh,Pembayaran_Jemaah_Umroh


admin.site.register(Haji)
admin.site.register(Jemaah_Hajis)
admin.site.register(Pembayaran_Jemaah_Haji)
# admin.site.register(Pembayaran)

# Register your models here.

admin.site.register(Umroh)
admin.site.register(Jemaah_Umroh)
admin.site.register(Pembayaran_Jemaah_Umroh)


