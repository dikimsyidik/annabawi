from datetime import datetime


def waktu(request):
    tanggal = datetime.now()
    bulan = tanggal.strftime("%m")
    tahun = tanggal.strftime('%Y')
    print(bulan)

    return {
        'time': tanggal,
        'bulannya': bulan,
        'tahunnya':tahun,
    }