class Data :
    def __init__(self, nama, nilai, sks):
        self.nama = nama
        self.nilai = nilai
        self.sks = sks

class IPK :
    def __init__(self):
        self.matkul1 = None
        self.matkul2 = None
    
    def data(self):
        nama = input('Masukkan nama mata kuliah : ')
        nilai = int(input('Masukkan nilai : '))
        sks = int(input('Masukkan sks : '))
        self.matkul1 = Data(nama, nilai, sks)

        nama = input('Masukkan nama mata kuliah : ')
        nilai = int(input('Masukkan nilai : '))
        sks = int(input('Masukkan sks : '))
        self.matkul2 = Data(nama, nilai, sks)
    
    def nilaiBobot1(self):
        self.bobot1 = []
        nilai1 = self.matkul1
        if nilai1.nilai >= 81 :
            self.bobot1 = 4
        elif nilai1.nilai >= 61 and nilai1.nilai <= 80 :
            self.bobot1 = 3
        elif nilai1.nilai >= 41 and nilai1.nilai <= 60 :
            self.bobot1 = 2
        elif nilai1.nilai >= 21 and nilai1.nilai <= 40 :
            self.bobot1 = 1
        else :
            self.bobot1 = 0
        print(f'Bobot mata kuliah Anda : {self.bobot1}')
        bobot = self.bobot1
        return bobot
    
    def nilaiBobot2(self):
        self.bobot2 = []
        nilai2 = self.matkul2
        if nilai2.nilai >= 81 :
            self.bobot2 = 4
        elif nilai2.nilai >= 61 and nilai2.nilai <= 80 :
            self.bobot2 = 3
        elif nilai2.nilai >= 41 and nilai2.nilai <= 60 :
            self.bobot2 = 2
        elif nilai2.nilai >= 21 and nilai2.nilai <= 40 :
            self.bobot2 = 1
        else :
            self.bobot2 = 0
        print(f'Bobot mata kuliah Anda : {self.bobot2}')
        bobot = self.bobot2
        return bobot

    def main(self):
        self.data()
        self.nilaiBobot1()
        self.nilaiBobot2()

        ntSks = self.matkul1.sks + self.matkul2.sks
        print(f'Total Sks : {ntSks}')

        bobotSks1 = self.bobot1 * self.matkul1.sks
        bobotSks2 = self.bobot2 * self.matkul2.sks
        ntBSKs = bobotSks1 + bobotSks2
        print(f'Total bobot sks Anda : {ntBSKs}')

        ipkAkhir = ntBSKs/ntSks
        print(f'IPK Akhir Anda : {ipkAkhir}')

if __name__ == '__main__':
    mulai = IPK()
    mulai.main()