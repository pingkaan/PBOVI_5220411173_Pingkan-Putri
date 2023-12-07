def main() :
    kop()
    print('\nSilakan masukkan data diri Anda')
    nama = input('Masukkan nama Anda = ')
    pekerjaan = input('Masukkan jenis pekerjaan Anda = ')
    penghasilan = float(input('Masukkan penghasilan Anda perbulan = '))
    
    penghasilanNasabah(penghasilan)


def penghasilanNasabah(penghasilan) :
    if penghasilan >= 500000000 :
        layanan = 3
        print(f'\nAnda dapat memilih {layanan} layanan pada Bank Sejahtera')
    elif 100000000 >= penghasilan <= 499999999 :
        layanan = 2
        print(f'\nAnda dapat memilih {layanan} layanan pada Bank Sejahtera')
    elif penghasilan < 100000000 :
        layanan = 1
        print(f'\nAnda dapat memilih {layanan} layanan pada Bank Sejahtera')
    else :
        print('\nNominal yang Anda masukkan tidak sesuai dengan format')
        main()
    
    for i in range(layanan) :
        pilihan()
        break
    
    jumlah = pilihan() + pilihan()
    print(f'Anda telah memilih layanan pada Bank Sejahtera dan dapat melakukan pembayaran sebagai berikut {jumlah}')

def kop() :
    print('=================================================')
    print('            Selamat Datang di Layanan            ')
    print('                 Bank Sejahtera                  ')
    print('=================================================')

def menuLayanan() :
    print('=================================================')
    print('\n1. Safe Deposit Box')
    print('2. Bank Garansi')
    print('3. Simpan Pinjam')
    print('4. Transfer')

def pilihan() :
    menuLayanan()
    namaLayanan = int(input('\nSilakan masukkan layanan yang ingin Anda pilih (1-4) : '))
    lamaLangganan = int(input('Masukkan waktu lama langganan yang akan Anda lakukan (1-12) : '))
    
    menuJenisLayanan()
    pilihJenis = int(input('\nMasukkan jenis langganan (1-3) : '))
    if pilihJenis == 1 :
        harga = 10000
        print(f'Anda telah memilih jenis layanan Platinum dengan biaya perbulan sebesar {harga}')
    elif pilihJenis == 2 :
        harga = 5000
        print(f'Anda telah memilih jenis layanan Gold dengan biaya perbulan sebesar {harga}')
    elif pilihJenis == 3 :
        harga = 3000
        print(f'Anda telah memilih jenis layanan Silver dengan biaya perbulan sebesar {harga}')
    return harga

def menuJenisLayanan() :
    print('\n1. Platinum, dengan biaya perbulan sebesar 10000')
    print('2. Gold, dengan biaya perbulan sebesar 5000')
    print('3. Silver, dengan biaya perbulan sebesar 3000')

if __name__ == '__main__':
    main()