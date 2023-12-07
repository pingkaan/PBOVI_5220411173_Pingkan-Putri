def main() :
    nama = input('Masukkan nama anda = ')
    nilai = int(input('Masukkan nilai anda = '))

    if nilai >= 75 :
        print('\nNama anda', nama)
        print('Anda mendapatkan peminatan Web Mobile')
    else :
        print('\nNama anda', nama)
        print('Anda mendapatkan peminatan Sistem Cerdas')

if __name__ == '__main__' :
    main()
