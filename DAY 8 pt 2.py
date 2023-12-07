class PerpusItem:
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek
    
    def lokasiPenyimpan(self):
        self.lokasi = PerpusItem(self.judul, self.subjek)
        print('\nLokasi penyimpanan:', self.lokasi)
    
    def info(self):
        print('Judul:', self.judul,
              '\nSubjek:', self.subjek)

class Buku(PerpusItem):
    def __init__(self, judul, subjek, isbn, pengarang, jmlHal, ukuran):
        super().__init__(judul, subjek)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran
    
    def info(self):
        print('Judul:', self.judul,
              '\nSubjek:', self.subjek,
              '\nISBN:', self.isbn,
              '\nPengarang:', self.pengarang,
              '\nJumlah halaman:', self.jmlHal,
              '\nUkuran:', self.ukuran)

class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issues):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issues = issues
    
    def info(self):
        print('Judul:', self.judul,
              '\nSubjek:', self.subjek,
              '\nVolume:', self.volume,
              '\nIssues:', self.issues)

class DVD(PerpusItem):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__(judul, subjek)
        self.genre = genre
        self.aktor = aktor
    
    def info(self):
        print('Judul:', self.judul,
              '\nSubjek:', self.subjek,
              '\nGenre:', self.genre,
              '\nAktor:', self.aktor)

class Katalog:
    def __init__(self):
        self.items = []
    
    def tambahItem(self, item):
        self.items.append(item)

    def cari(self):
        pencarian = input('Masukkan judul yang dicari: ')
        for i in self.items:
            if i.judul == pencarian:
                return i
        return 'Item tidak ada'

class Pengarang:
    def __init__(self, nama):
        self.nama = nama
        self.karya = []
    
    def tambahKarya(self, item):
        self.karya.append(item)

    def info(self):
        print('Nama Pengarang:', self.nama)
        print('Karya pengarang:', [item.judul for item in self.karya])
    
    def cari(self, judul):
        for item in self.karya:
            if item.judul == judul:
                return item
        return 'Karya tidak ada'

class Menu:
    @staticmethod
    def menuUtama():
        print('='*20)
        print('1. Input Perpus Item',
              '\n2. Daftar Katalog',
              '\n3. Cari Pengarang')
        print('='*20)

item = Katalog()

while True:
    Menu.menuUtama()
    pilih = int(input('Masukkan pilihan: '))

    if pilih == 1:
        judul = input('Masukkan judul: ')
        subjek = input('Masukkan subjek: ')

        if subjek == 'Buku':
            isbn = input('Masukkan ISBN: ')
            pengarang = input('Masukkan nama pengarang: ')
            jmlHal = int(input('Masukkan jumlah halaman: '))
            ukuran = input('Masukkan ukuran buku: ')

            dataBuku = Buku(judul, subjek, isbn, pengarang, jmlHal, ukuran)
            item.tambahItem(dataBuku)

            dataPengarang = Pengarang(pengarang)
            dataPengarang.tambahKarya(dataBuku)
        
        elif subjek == 'Majalah':
            volume = input('Masukkan volume edisi: ')
            issues = input('Masukkan tema issues: ')

            dataMajalah = Majalah(judul, subjek, volume, issues)
            item.tambahItem(dataMajalah)
        
        elif subjek == 'DVD':
            aktor = input('Masukkan nama aktor: ')
            genre = input('Masukkan genre film: ')

            dataDVD = DVD(judul, subjek, aktor, genre)
            item.tambahItem(dataDVD)

    elif pilih == 2:
        result = item.cari()
        if result != 'Item tidak ada':
            result.info()
        else:
            print(result)
    
    elif pilih == 3:
        pencarian = input('Masukkan nama pengarang yang dicari: ')
        result = dataPengarang.cari(pencarian)
        if result != 'Karya tidak ada':
            result.info()
        else:
            print(result)
