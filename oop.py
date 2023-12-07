import sys

class User :
    def __init__(self):
        self.nama = input('\nMasukkan nama Anda: ')
        self.pekerjaan = input('Masukkan pekerjaan Anda: ')
        self.penghasilan = int(input('Masukkan penghasilan bulanan Anda: '))

class Layanan :
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Langganan :
    def __init__(self):
        self.pilihLayanan = None
        self.waktuLangganan = None
        self.jenisLangganan = None

class ApkLayananBank :
    def __init__(self):
        self.user = User()
        self.layanan = [
            Layanan("Safe Deposit Box", 10000),
            Layanan("Bank Garansi", 5000),
            Layanan("Simpan Pinjam", 3000),
            Layanan("Transfer", 0)
        ]

    def main(self):
        self.kop()
        self.pilihLayanan()
        self.pilihan()

    def kop(self):
        print('=================================================')
        print('            Selamat Datang di Layanan            ')
        print('                 Bank Sejahtera                  ')
        print('=================================================')

    def pilihLayanan(self):
        print('Pilih layanan yang diinginkan:')
        for i, layanan in enumerate(self.layanan, start=1):
            print(f"{i}. {layanan.nama}")

    def pilihan(self):
        pilih = int(input('Masukkan jenis layanan yang diinginkan (1-4): '))
        if 1 <= pilih <= 4:
            pilihLangganan = Langganan()
            pilihLangganan.pilihLayanan = self.layanan[pilih - 1]
            pilihLangganan.waktuLangganan = int(input('Masukkan waktu berlangganan (1-12): '))
            self.menuLangganan()
            pilihLangganan.jenisLangganan = int(input('\nMasukkan jenis langganan: '))
            self.hargaLayanan(pilihLangganan)
        elif pilih == 0:
            sys.exit('Anda telah mengakhiri pilihan. Terimakasih dan sampai jumpa!')
        else:
            print('Anda telah memilih layanan tersebut')
            self.pilihan()

    def menuLangganan(self):
        print('=================================================')
        print('1. Platinum, dengan biaya perbulan sebesar 10000')
        print('2. Gold, dengan biaya perbulan sebesar 5000')
        print('3. Silver, dengan biaya perbulan sebesar 3000')

    def hargaLayanan(self, langganan):
        total = langganan.waktuLangganan * langganan.pilihLayanan.harga
        print(f'Total harga layanan yang Anda pilih adalah {total}')

if __name__ == '__main__':
    app = ApkLayananBank()
    app.main()
