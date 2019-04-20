from django.urls import path

from data_jemaah.views import (
							list_haji,
							tambah_haji
							,detail_haji,
							list_umroh,
							tambah_umroh,
							detail_umroh,
                            edit_haji,
                            edit_umroh,
                            hapus_umroh,
                            hapus_haji,
							)
from data_jemaah.views import (
							pembayaran_haji,
							pembayaran_umroh,
							pemasukan_haji,
							pemasukan_umroh,
							kwitansi_haji,
                            kwitansi_umroh,


                            jemaah_haji,
                            jemaah_haji_tambah,
                            jemaah_haji_detail,
                            jemaah_haji_edit,
                            jemaah_haji_hapus,

                            jemaah_umroh,
                            jemaah_umroh_tambah,
                            jemaah_umroh_detail,
                            jemaah_umroh_edit,
                            jemaah_umroh_hapus,
                            
                            )

from.views import (
                    dashboard,
                    rekap,
                    tiket_arsip,
                    tiket_tambah,
                    tiket_hapus,
                    la_view,
                    la_tambah,
                    la_hapus,
                    kendaraan,
                    kendaraan_tambah,
                    kendaraan_hapus,
                    pembukuan_umroh,
                    pembukuan_umroh_tambah,
                    pembukuan_umroh_hapus,
                    handling,
                    handling_tambah,
                    handling_hapus,
                    paspor,
                    paspor_tambah,
                    paspor_hapus,
                    transfortasi,
                    transfortasi_tambah,
                    transfortasi_edit,
                    transfortasi_hapus,
                    pembukuan_haji,
                    pembukuan_haji_tambah,
                    pembukuan_haji_hapus,
                    pembukuan_pajak,
                    pembukuan_pajak_tambah,
                    pembukuan_pajak_hapus,
                    atk,
                    atk_tambah,
                    atk_hapus,
                    pembukuan_honor_karyawan,
                    pembukuan_honor_karyawan_tambah,
                    pembukuan_honor_karyawan_hapus,
            )
urlpatterns = [
    path('', dashboard,name='dashboard'),
    path('rekap/', rekap,name='rekap'),

    path('jadwal_pemberangkatan_haji/', list_haji,name='jadwal_haji'),
    path('jadwal_pemberangkatan_haji/tambah_jadwal_haji', tambah_haji,name='tambah_haji'),
    path('jadwal_pemberangkatan_haji/<int:id>/', detail_haji,name='detail_haji'),
    path('jadwal_pemberangkatan_haji/edit/<int:id>/', edit_haji,name='detail_haji'),
    path('jadwal_pemberangkatan_haji/hapus/<int:id>/', hapus_haji,name='detail_haji'),

    path('jadwal_pemberangkatan_umroh/', list_umroh,name='jadwal_umroh'),
    path('jadwal_pemberangkatan_umroh/tambah_jadwal_umroh', tambah_umroh,name='tambah_umroh'),
    path('jadwal_pemberangkatan_umroh/<int:id>/', detail_umroh,name='detail_umroh'),
    path('jadwal_pemberangkatan_umroh/edit/<int:id>/', edit_umroh,name='detail_umroh'),
    path('jadwal_pemberangkatan_umroh/hapus/<int:id>/', hapus_umroh,name='detail_umroh'),

    path('pemasukan_haji/', pemasukan_haji,name='pemasukan_haji'),
    path('pemasukan_umroh/', pemasukan_umroh,name='pemasukan_umroh'),
    path('pembayaran_haji/', pembayaran_haji,name='pembayaran_haji'),
    path('pembayaran_umroh/', pembayaran_umroh,name='pembayaran_umroh'),
    path('pembayaran_haji/kwitansi_haji/<int:id>/', kwitansi_haji,name='kwitansi_haji'),
    path('pemasukan_umroh/kwitansi_umroh/<int:id>/', kwitansi_umroh,name='kwitansi_umroh'),

    path('list_jemaah_haji/', jemaah_haji,name='list_jemaah_haji'),
    path('list_jemaah_haji/tambah/', jemaah_haji_tambah,name='tambah_jemaah_haji'),
    path('list_jemaah_haji/<slug:id>/', jemaah_haji_detail,name='detail_jemaah_haji'),
    path('list_jemaah_haji/hapus/<slug:id>/', jemaah_haji_hapus,name='hapus_jemaah_haji'),
    path('list_jemaah_haji/edit/<slug:id>/', jemaah_haji_edit,name='edit_jemaah_haji'),


    path('list_jemaah_umroh/', jemaah_umroh,name='list_jemaah_umroh'),
    path('list_jemaah_umroh/tambah/', jemaah_umroh_tambah,name='tambah_jemaah_umroh'),
    path('list_jemaah_umroh/<slug:id>/', jemaah_umroh_detail,name='detail_jemaah_umroh'),
    path('list_jemaah_umroh/hapus/<slug:id>/', jemaah_umroh_hapus,name='hapus_jemaah_umroh'),
    path('list_jemaah_umroh/edit/<slug:id>/', jemaah_umroh_edit,name='edit_jemaah_umroh'),


    path('tiket/<int:year>/<int:month>/', tiket_arsip,name='tiket'),
    
    path('tiket/<int:year>/<int:month>/tambah/', tiket_tambah,name='tiket_tambah'),
    path('tiket/<int:year>/<int:month>/hapus/<int:id>/', tiket_hapus,name='tiket_hapus'),


    path('la/<int:year>/<int:month>/', la_view,name='la'),
    path('la/<int:year>/<int:month>/tambah/', la_tambah,name='tiket_tambah'),
    path('la/<int:year>/<int:month>/hapus/<int:id>/', la_hapus,name='tiket_hapus'),

    path('kendaraan/<int:year>/<int:month>/', kendaraan,name='kendaraan'),
    path('kendaraan/<int:year>/<int:month>/tambah/', kendaraan_tambah,name='tiket_tambah'),
    path('kendaraan/<int:year>/<int:month>/hapus/<int:id>/', kendaraan_hapus,name='tiket_hapus'),

    path('pembukuan_umroh/<int:year>/<int:month>/', pembukuan_umroh,name='pembukuan_umroh'),
    path('pembukuan_umroh/<int:year>/<int:month>/tambah/', pembukuan_umroh_tambah,name='tiket_tambah'),
    path('pembukuan_umroh/<int:year>/<int:month>/hapus/<int:id>/', pembukuan_umroh_hapus,name='tiket_hapus'),

    path('handling/<int:year>/<int:month>/', handling,name='handling'),
    path('handling/<int:year>/<int:month>/tambah/', handling_tambah,name='tiket_tambah'),
    path('handling/<int:year>/<int:month>/hapus/<int:id>/', handling_hapus,name='tiket_hapus'),

    path('paspor/<int:year>/<int:month>/', paspor,name='paspor'),
    path('paspor/<int:year>/<int:month>/tambah/', paspor_tambah,name='tiket_tambah'),
    path('paspor/<int:year>/<int:month>/hapus/<int:id>/', paspor_hapus,name='tiket_hapus'),

    path('transportasi/<int:year>/<int:month>/', transfortasi,name='transportasi'),
    path('transportasi/<int:year>/<int:month>/tambah/', transfortasi_tambah,name='tiket_tambah'),
    path('transportasi/<int:year>/<int:month>/hapus/<int:id>/', transfortasi_hapus,name='tiket_hapus'),

    path('pembukuan_haji/<int:year>/<int:month>/', pembukuan_haji,name='pembukuan_haji'),
    path('pembukuan_haji/<int:year>/<int:month>/tambah/', pembukuan_haji_tambah,name='tiket_tambah'),
    path('pembukuan_haji/<int:year>/<int:month>/hapus/<int:id>/', pembukuan_haji_hapus,name='tiket_hapus'),

    path('pembukuan_pajak/<int:year>/<int:month>/', pembukuan_pajak,name='pembukuan_pajak'),
    path('pembukuan_pajak/tambah/', pembukuan_pajak_tambah,name='tiket_tambah'),
    path('pembukuan_pajak/<int:year>/<int:month>/hapus/<int:id>/', pembukuan_pajak_hapus,name='tiket_hapus'),

    path('atk/<int:year>/<int:month>/', atk,name='atk'),
    path('atk/<int:year>/<int:month>/tambah/', atk_tambah,name='tiket_tambah'),
    path('atk/<int:year>/<int:month>/hapus/<int:id>/', atk_hapus,name='tiket_hapus'),

    path('pembukuan_honor_karyawan/<int:year>/<int:month>/', pembukuan_honor_karyawan,name='pembukuan_honor_karyawan'),
    path('pembukuan_honor_karyawan/<int:year>/<int:month>/tambah/', pembukuan_honor_karyawan_tambah,name='tiket_tambah'),
    path('pembukuan_honor_karyawan/<int:year>/<int:month>/hapus/<int:id>/', pembukuan_honor_karyawan_hapus,name='tiket_hapus'),

    ]