def main() :
    print(
        'Nomor Urut 1 Uzumaki Naruto'
        '\nNomor Urut 2 Gojo Satoru'
        '\nNomor Urut 3 Yu Nishinoya'
    )
    nama = input('\nMasukkan nama Anda = ')
    nomor = int(input('Masukkan nomor pemilih = '))
    pilih = int(input('Masukkan nomor pilihan Anda = '))

    if pilih == 1 :
        print('\nAnda telah memilih Uzumaki Naruto')
    elif pilih == 2 :
        print('\nAnda telah memilih Gojo Satoru')
    elif pilih == 3 :
        print('\nAnda telah memilih Yu Nishinoya')
    else :
        print('\nPilihan yang Anda masukkan tidak tersedia\n')
        main()

if __name__ == '__main__':
    main()