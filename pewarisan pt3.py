class Kamera:
    def __init__(self, nama, harga):
        self.nama = nama
        self._harga = harga

    def hitungBiayaSewa(self, hari):
        return self._harga * hari

class DSLR(Kamera):
    def __init__(self):
        super().__init__("DSLR", 200000)

class Mirrorless(Kamera):
    def __init__(self):
        super().__init__("Mirrorless", 300000)

class ActionCam(Kamera):
    def __init__(self):
        super().__init__("Action Cam", 350000)

def main():
    kop()
    nama = input("Masukkan nama Anda : ")
    id = int(input("Masukkan ID Anda : "))
    menu()

def menu():
    while True :
        print("\n1. Sewa Kamera")
        print("0. Keluar")
        pilih = int(input("Masukkan pilihan Anda : "))
        if pilih == 1 :
            sewaKamera()
        elif pilih == 0 :
            exit("Terimakasih telah mampir!")
        else :
            print("Pilihan tidak ada!")
            continue

def kop():
    print('=================================================')
    print('           Selamat Datang di Penyewaan           ')
    print('                 Kamera Jaya-3x                  ')
    print('=================================================')

def sewaKamera():
    while True :
        print("\nBerikut pilihan kamera yang tersedia: ")
        print("1. DSLR")
        print("2. Mirrorless")
        print("3. Action Cam")
        pilih = int(input("\nMasukkan pilihan Anda (1-3): "))
        if pilih == 1:
            kamera = DSLR()
        elif pilih == 2:
            kamera = Mirrorless()
        elif pilih == 3:
            kamera = ActionCam()
        else:
            print("Pilihan tidak ada!")
            act = input("\nApakah Anda ingin melakukan sewa lagi? (y/n): ")
            if act == "y" :
                continue
            else :
                break
        
        hari = int(input("Masukkan jumlah hari penyewaan: "))
        biaya = kamera.hitungBiayaSewa(hari)
        print(f"Anda telah menyewa kamera {kamera.nama} dengan biaya total {biaya}")
        
        act = input("\nApakah Anda ingin melakukan sewa lagi? (y/n): ")
        if act == "y" :
            continue
        else :
            break

if __name__ == "__main__":
    main()