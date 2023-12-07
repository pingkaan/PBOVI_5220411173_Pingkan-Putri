# tipe data string = 3x + X^2 bilangan real dan bilangan imajiner
# () = tuple
# {} = dict
# [] = list

# 3,4 - 4 = bisa memilih 6 mata kuliah
# 3 - 3,49 = bisa input 4 mk 
# 2, 5 - 2,9 = 3 mk 
# dibawahnya cm 2 kali

def main() :
    # nama = input('Masukkan nama Anda: ')
    # npm = input('Masukkan NPM Anda: ')
    ipk = float(input('Masukkan IPK Anda: '))

    if ipk >= 3.5 and ipk <= 4 :
        print('Anda dapat mengambil 6 mata kuliah')

        jml = 6
        mataKuliah()
        pilihan = int(input('MAsukkan : '))
        if 1 <= pilihan <= 6 :
            
        


    elif ipk <= 3.4 and ipk >= 3.0 :
        print('Anda dapat mengambil 4 mata kuliah')
    elif ipk < 3.0 and ipk >= 2.5 :
        print('Anda dapat mengambil 3 mata kuliah')
    elif ipk < 2.5 and ipk >= 1.0 :
        print('Anda dapat mengambil 2 mata kuliah')
    else :
        print('Nilai IPK Anda berbeda dari umumnya')
    

def mataKuliah() :
    print('==========================================================')
    print('                MATA KULIAH YANG TERSEDIA                 ')
    print('==========================================================')
    print('     1. Algoritma Pemrograman')
    print('     2. Struktur dan Basis Data')
    print('     3. Teknologi Berbasis Objek')
    print('     4. Metodelogi Desain Perangkat Lunak')
    print('     5. Pemrograman Berbasis Objek')
    print('     6. Kalkulus II')


if __name__ == '__main__':  
    main()