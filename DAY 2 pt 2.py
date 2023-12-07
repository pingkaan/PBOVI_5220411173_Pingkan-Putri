def main() :
    nama = input("Masukkan nama Anda: ")
    kategori()
    pilihKategori = int(input("\nMasukkan kategori yang akan diambil: "))
    if pilihKategori == 1 :
        print('Anda telah memilih kategori Premium')
        # i = pilihKategori
        for i in range(3) :
            cicilanWoy()
        print('Anda telah melakukan seluruh pembayaran')
    elif pilihKategori == 2 :
        print('Anda telah memilih kategori Exclusive')
        i = pilihKategori
        for i in range(4) :
            cicilanWoy()
        print('Anda telah melakukan seluruh pembayaran')
    elif pilihKategori == 3 :
        print('Anda telah memilih kategori Reguler')
        i = pilihKategori
        for i in range(6) :
            cicilanWoy()
        print('Anda telah melakukan seluruh pembayaran')
    else :
        print('Pilihan yang Anda masukkan tidak tersedia')
        main

def cicilanWoy() :
    cicilan = [
        "Bayar cicilan yang pertama",
        "Bayar cicilan yang kedua",
        "Bayar cicilan yang ketiga",
        "Bayar cicilan yang keempat",
        "Bayar cicilan yang kelima",
        "Bayar cicilan yang keenam"
    ]
    
    pilihan = int(input('\nMasukkan cicilan yang akan dibayar (1-6): '))
    if 1 <= pilihan <= 6 :
        bayarCicilan = cicilan[pilihan-1]
        print(f"Anda telah: {bayarCicilan}")
    else :
        print('Pilihan Anda salah')

def kategori() :
    print('================================================')
    print('                DAFTAR KATEGORI                 ')
    print('================================================')
    print("   1. Kategori Premium -> Cicilan 3x 1 Tahun")
    print("   2. Kategori Exclusive -> Cicilan 4x 1 Tahun")
    print("   3. Kategori Reguler -> Cicilan 6x 1 Tahun")

if __name__ == "__main__":
    main()