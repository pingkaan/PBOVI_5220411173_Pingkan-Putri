import datetime

class Kuliner:
    def __init__(self, idProduk, nama, jenisProduk):
        self.idProduk = idProduk
        self.nama = nama
        self.jenisProduk = jenisProduk
    
    def infoProduk(self):
        print(f"\nID Produk = {self.idProduk}")
        print(f"Nama = {self.nama}")
        print(f"Jenis Produk = {self.jenisProduk}")

class Makanan(Kuliner):
    def __init__(self, idProduk, nama, jenisProduk, harga, masaExp, stok, lamaBuat):
        super().__init__(idProduk, nama, jenisProduk)
        self.harga = harga
        self.masaExp = masaExp
        self._stok = stok
        self.__lamaBuat = lamaBuat
    
    def infoProduk(self):
        super().infoProduk()
        print(f"Harga = {self.harga} IDR")
        print(f"Expired Day = {self.masaExp}")
        print(f"Stok = {self._stok}")
    
    def getLamaBuat(self):
        return self.__lamaBuat
    
    def preOrder(self, pesanan):
        pesanan = int(input("Masukkan jumlah pesanan preorder : "))
        if pesanan >= 10:
            jumlahPesanan = pesanan // 10
            tambahanHari = jumlahPesanan * self.__lamaBuat
            print(f"Setiap pesanan kelipatan 50 akan menambah {tambahanHari} hari waktu tunggu.")
            print(f"Anda memiliki total {tambahanHari} hari waktu tunggu.")
        else:
            print(f"Produk {self.nama} tersedia untuk pembelian. Silakan lakukan pembelian sekarang")

class Minuman(Kuliner):
    def __init__(self, idProduk, nama, jenisProduk, harga, masaExp, stok, lamaBuat):
        super().__init__(idProduk, nama, jenisProduk)
        self.harga = harga
        self.masaExp = masaExp
        self._stok = stok
        self.__lamaBuat = lamaBuat
    
    def infoProduk(self):
        super().infoProduk()
        print(f"Harga = {self.harga} IDR")
        print(f"Expired Day = {self.masaExp}")
        print(f"Stok = {self._stok}")
    
    def getLamaBuat(self):
        return self.__lamaBuat
    
    def preOrder(self, pesanan):
        pesanan = int(input("Masukkan jumlah pesanan preorder : "))
        if pesanan >= 10:
            jumlahPesanan = pesanan // 10
            tambahanHari = jumlahPesanan * self.__lamaBuat
            print(f"Setiap pesanan kelipatan 50 akan menambah {tambahanHari} hari waktu tunggu.")
            print(f"Anda memiliki total {tambahanHari} hari waktu tunggu.")
        else:
            print(f"Produk {self.nama} tersedia untuk pembelian. Silakan lakukan pembelian sekarang")

class MinumanBersoda(Minuman):
    def __init__(self, idProduk, nama, jenisProduk, harga, masaExp, stok, lamaBuat, batasKonsumen):
        super().__init__(idProduk, nama, jenisProduk, harga, masaExp, stok, lamaBuat)
        self.batasKonsumen = batasKonsumen
    
    def infoProduk(self):
        super().infoProduk()
        print(f"Harga = {self.harga} IDR")
        print(f"Expired Day = {self.masaExp}")
        print(f"Stok = {self._stok}")
        print(f"Batas Usia Konsumen = {self.batasKonsumen}")
    
    def getLamaBuat(self):
        return self.__lamaBuat
    
    def preOrder(self, pesanan):
        super().preOrder(pesanan)
        idPembeli = int(input("Masukkan ID Anda : "))
        usia = int(input("Masukkan usia Anda : "))
        if usia >= 19 :
            print("Pesanan telah diterima. Silakan menunggu")
        else :
            print("Maaf, usia Anda belum mencukupi. Anda tidak dapat melakukan pemesanan")

class ProdukKuliner:
    def __init__(self):
        self.items = []
    
    def tambahProduk(self, item):
        self.items.append(item)
    
    def hapusProduk(self, idProduk):
        for item in self.items:
            if item.idProduk == idProduk:
                self.items.remove(item)
                break
    
    def daftarProduk(self):
        if len(self.items) == 0:
            print("Data tidak tersedia")
        else :
            for item in self.items:
                item.infoProduk()
    
    def cariProduk(self, cari):
        for item in self.items:
            if item.idProduk == cari:
                return item
        return None
    
    def updateStokProduk(self, idProduk, stokBaru):
        item = self.cariProduk(idProduk)
        if item != 'Item tidak ada' :
            jumlahStok = item._stok + stokBaru
            item._stok = jumlahStok
            print("Stok produk berhasil diupdate")
    
    def beliProduk(self, idProduk, jumlahBeli):
        item = self.cariProduk(idProduk)
        if item is not None :
            jumlahStok = item._stok - jumlahBeli
            item._stok = jumlahStok

class Menu:
    def kop():
        print("=====================================")
        print("         Selamat Datang di           ")
        print("          Culinary Crafts            ")
        print("=====================================")
    
    def menuUtama():
        print("\t \t>> Menu Utama")
        print("\t \t---------------------")
        print("\n1. Atur Produk",
              "\n2. Daftar Produk",
              "\n3. Beli Produk",
              "\n0. Keluar")
    
    def aturProduk():
        print("\t \t>> Atur Produk")
        print("\t \t---------------------")
        print("\n1. Tambah Produk",
              "\n2. Hapus Produk",
              "\n3. Update Stok Produk",
              "\n0. Kembali")
    
    def beliProduk():
        print("\t \t>> Beli Produk")
        print("\t \t---------------------")
        print("\n1. Beli Sekarang",
              "\n2. Pre Order",
              "\n0. Kembali")
    
    def exit():
        print("=========================================")
        print("     Terimakasih Telah Berbelanja        ")
        print("          di Culinary Crafts             ")
        print("=========================================")

produk = ProdukKuliner()

while True:
    Menu.kop()
    Menu.menuUtama()
    
    pilih = int(input("\nMasukkan pilihan : "))
    if pilih == 1 :
        while True :
            Menu.kop()
            Menu.aturProduk()
            
            pilihan = int(input("\nMasukkan pilihan : "))
            if pilihan == 1 :
                while True :
                    Menu.kop()
                    print("\t \t>> Tambah Produk")
                    print("\t \t---------------------")
                    
                    id = int(input("\nMasukkan ID produk : "))
                    nama = input("Masukkan nama produk : ")
                    jenis = input("Masukkan jenis produk : ")
                    harga = int(input("Masukkan harga produk : "))
                    
                    print("\nMasukkan data expired day!")
                    masaExpTgl = int(input("Masukkan tanggal : "))
                    masaExpBln = int(input("Masukkan bulan : "))
                    masaExpThn = int(input("Masukkan tahun : "))
                    masaExp = datetime.datetime(masaExpThn, masaExpBln, masaExpTgl)
                    
                    stok = int(input("\nMasukkan jumlah stok produk : "))
                    pembuatan = int(input("Masukkan lama pembuatan produk (hari): "))
                    
                    if jenis.lower() == "makanan" :
                        item = Makanan(id, nama, jenis, harga, masaExp, stok, pembuatan)
                        produk.tambahProduk(item)
                    
                    elif jenis.lower() == "minuman" :
                        batasan = int(input("Masukkan batasan umur konsumen : "))
                        if batasan <= 12 :
                            item = Minuman(id, nama, jenis, harga, masaExp, stok, pembuatan)
                        
                        elif batasan > 12 :
                            jenis = "Minuman bersoda"
                            item = MinumanBersoda(id, nama, jenis, harga, masaExp, stok, pembuatan, batasan)
                        
                        produk.tambahProduk(item)
                        print("\nData produk baru telah ditambahkan")
                    
                    else :
                        print("\nMaaf kita tidak menyediakan produk ini")
                    
                    choice = input("\nApakah Anda ingin menambah produk lagi? (y/n) : ")
                    if choice.lower() == "y" :
                        continue
                    elif choice.lower() == "n" :
                        break
                
            elif pilihan == 2 :
                Menu.kop()
                print("\t \t>> Hapus Produk")
                print("\t \t---------------------")
                produk.daftarProduk()
                
                id = int(input("\nMasukkan ID produk : "))
                produk.hapusProduk(id)
                print("\nData produk telah terhapus")
                
                choice = input("\nApakah Anda ingin menghapus produk lagi? (y/n) : ")
                if choice.lower() == "y" :
                    continue
                elif choice.lower() == "n" :
                    break
            
            elif pilihan == 3 :
                Menu.kop()
                print("\t \t>> Update Stok Produk")
                print("\t \t---------------------")
                produk.daftarProduk()
                
                idProduk = int(input("\nMasukkan ID Produk yang akan diupdate : "))
                stokBaru = int(input("Masukkan stok baru: "))
                produk.updateStokProduk(idProduk, stokBaru)
                print("\nStok produk telah diupdate")
                
                choice = input("\nApakah Anda ingin mengupdate stok produk lagi? (y/n) : ")
                if choice.lower() == "y" :
                    continue
                elif choice.lower() == "n" :
                    break
            
            elif pilihan == 0 :
                break
            
            else :
                print("Maaf pilihan ini tidak tersedia")
                continue
    
    elif pilih == 2 :
        Menu.kop()
        print("\t \t>> Daftar Produk")
        print("\t \t---------------------")
        produk.daftarProduk()
    
    elif pilih == 3 :
        Menu.kop()
        Menu.beliProduk()
        
        pilihan3 = int(input("\nMasukkan pilihan : "))
        if pilihan3 == 1 :
            while True :
                Menu.kop()
                print("\t \t>> Beli Sekarang")
                print("\t \t---------------------")
                produk.daftarProduk()
                
                idProduk = int(input("\nMasukkan ID Produk yang akan dibeli (0 untuk kembali): "))
                if idProduk == 0:
                    break
                jumlahBeli = int(input("Masukkan jumlah produk yang akan dibeli: "))
                produk.beliProduk(idProduk, jumlahBeli)

                print("\nPembelian telah dilakukan. Berikut rinciannya:")
                beliItem = produk.cariProduk(idProduk)
                print(f"\nID Produk: {beliItem.idProduk}")
                print(f"Nama: {beliItem.nama}")
                print(f"Jumlah Beli: {jumlahBeli}")
                print(f"Total Harga: {jumlahBeli * beliItem.harga} IDR")
                
                choice = input("\nApakah Anda ingin membeli produk lagi? (y/n) : ")
                if choice.lower() == "y" :
                    continue
                elif choice.lower() == "n" :
                    break
        
        elif pilihan3 == 2:
            while True:
                Menu.kop()
                print("\t \t>> Pre Order")
                print("\t \t---------------------")
                produk.daftarProduk()
                
                idProduk = int(input("\nMasukkan ID Produk yang akan dibeli (0 untuk kembali): "))
                item = produk.cariProduk(idProduk)

                if idProduk == 0 or item is None:
                    break

                print(f"Lama Pembuatan per 10 buah produk: {item.getLamaBuat()} hari")
                item.preOrder()

                print("\nPemesanan telah dilakukan. Berikut rinciannya:")
                print(f"\nID Produk: {item.idProduk}")
                print(f"Nama: {item.nama}")
                print(f"Harga: {item.harga} IDR")
                print(f"Expired Day: {item.masaExp}")
                print(f"Jumlah Hari Tunggu: {item._Kuliner__lamaBuat} hari")
                
                choice = input("\nApakah Anda ingin memesan produk lagi? (y/n) : ")
                if choice.lower() == "y":
                    continue
                elif choice.lower() == "n":
                    break

        
        elif pilihan == 0 :
            break
        
        else :
            print("Maaf pilihan ini tidak tersedia")
            continue
    
    elif pilih == 0 :
        exit(Menu.exit())
    
    else :
        continue