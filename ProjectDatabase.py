from mysql.connector import Connect, Error
from prettytable import PrettyTable
import datetime
import os

def koneksi():
    koneksidb = None
    try :
        koneksidb = Connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "5220411173_kuliner"
            )
    except Error as e :
        print(e)
    return koneksidb

class Kuliner:
    def __init__(self, idProduk, nama, jenisProduk):
        self.idProduk = idProduk
        self.nama = nama
        self.jenisProduk = jenisProduk

class Makanan(Kuliner):
    def __init__(self, idProduk=None, nama=None, jenisProduk=None, harga=None, masaExp=None, stok=None, lamaBuat=None):
        super().__init__(idProduk, nama, jenisProduk)
        self.harga = harga
        self.masaExp = masaExp
        self._stok = stok
        self.__lamaBuat = lamaBuat
    
    def infoProduk(self):
        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM makanan")
                results = cursor.fetchall()
                
                if not results:
                    print("Tidak ada data makanan.")
                    return
                
                table = PrettyTable()
                table.field_names = ["ID", "NAMA", "JENIS", "HARGA", "EXPIRED DAY", "STOK", "LAMA BUAT"]
                
                for result in results:
                    table.add_row([result[0], result[1], result[2], result[3], result[4], result[5], result[6]])
                    
                print(table)
                
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
    
    def tambahProduk(self):
        id = input("\nMasukkan ID produk: ")
        nama = input("Masukkan nama produk: ")
        jenis = input("Masukkan jenis produk: ")
        harga = int(input("Masukkan harga produk: "))
        
        print("\nMasukkan data expired day!")
        masaExpTgl = int(input("Masukkan tanggal : "))
        masaExpBln = int(input("Masukkan bulan : "))
        masaExpThn = int(input("Masukkan tahun : "))
        masaExp = datetime.date(masaExpThn, masaExpBln, masaExpTgl)
        
        stok = int(input("\nMasukkan stok produk: "))
        lamaBuat = input("Masukkan lama pembuatan produk: ")
        
        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO makanan (idProduk, namaProduk, jenisProduk, harga, masaExp, stok, lamaBuat) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                               (id, nama, jenis, harga, masaExp, stok, lamaBuat))
                connection.commit()
                print(f"Produk {nama} berhasil ditambahkan.")
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
    
    def hapusProduk(self):
        idProduk = input("Masukkan ID produk yang akan dihapus: ")
        
        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM makanan WHERE idProduk = %s", (idProduk,))
                connection.commit()
                print(f"Produk dengan ID {idProduk} berhasil dihapus.")
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
    
    def updateStokProduk(self):
        idProduk = input("Masukkan ID produk yang akan diupdate: ")
        stokBaru = int(input("Masukkan stok baru: "))
        
        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE makanan SET stok = %s WHERE idProduk = %s", (stokBaru, idProduk))
                connection.commit()
                print(f"Stok produk dengan ID {idProduk} berhasil diupdate.")
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

class Minuman(Kuliner):
    def __init__(self, idProduk=None, nama=None, jenisProduk=None, harga=None, masaExp=None, stok=None, lamaBuat=None):
        super().__init__(idProduk, nama, jenisProduk)
        self.harga = harga
        self.masaExp = masaExp
        self._stok = stok
        self.__lamaBuat = lamaBuat
    
    def infoProduk(self):
        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM minuman")
                results = cursor.fetchall()
                
                if not results:
                    print("Tidak ada data minuman.")
                    return
                
                table = PrettyTable()
                table.field_names = ["ID", "NAMA", "JENIS", "HARGA", "EXPIRED DAY", "STOK", "LAMA BUAT"]
                
                for result in results:
                    table.add_row([result[0], result[1], result[2], result[3], result[4], result[5], result[6]])
                    
                print(table)
                
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
    
    def tambahProduk(self):
        id = input("\nMasukkan ID produk: ")
        nama = input("Masukkan nama produk: ")
        jenis = input("Masukkan jenis produk: ")
        harga = int(input("Masukkan harga produk: "))
        
        print("\nMasukkan data expired day!")
        masaExpTgl = int(input("Masukkan tanggal : "))
        masaExpBln = int(input("Masukkan bulan : "))
        masaExpThn = int(input("Masukkan tahun : "))
        masaExp = datetime.date(masaExpThn, masaExpBln, masaExpTgl)
        
        stok = int(input("\nMasukkan stok produk: "))
        lamaBuat = input("Masukkan lama pembuatan produk: ")

        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO minuman (idProduk, namaProduk, jenisProduk, harga, masaExp, stok, lamaBuat) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                               (id, nama, jenis, harga, masaExp, stok, lamaBuat))
                connection.commit()
                print(f"Produk {nama} berhasil ditambahkan.")
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
    
    def hapusProduk(self):
        idProduk = input("Masukkan ID produk yang akan dihapus: ")

        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM minuman WHERE idProduk = %s", (idProduk,))
                connection.commit()
                print(f"Produk dengan ID {idProduk} berhasil dihapus.")
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
    
    def updateStokProduk(self):
        idProduk = input("Masukkan ID produk yang akan diupdate: ")
        stokBaru = int(input("Masukkan stok baru: "))
        
        try:
            connection = koneksi()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE minuman SET stok = %s WHERE idProduk = %s", (stokBaru, idProduk))
                connection.commit()
                print(f"Stok produk dengan ID {idProduk} berhasil diupdate.")
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

class Menu:
    def kop():
        print("=====================================")
        print("         Selamat Datang di           ")
        print("          Culinary Crafts            ")
        print("=====================================")
    
    def menuJenis():
        print("\t \t>> Pilih Jenis")
        print("\t \t---------------------")
        print("\n1. Makanan",
              "\n2. Minuman",
              "\n0. Keluar")
    
    def menuPengaturan():
        print("\t \t>> Menu Pengaturan")
        print("\t \t---------------------")
        print("\n1. Tambah Produk",
              "\n2. Hapus Produk",
              "\n3. Update Stok Produk",
              "\n4. Daftar Produk",
              "\n0. Kembali")
    
    def exit():
        print("=========================================")
        print("     Terimakasih Telah Berbelanja        ")
        print("          di Culinary Crafts             ")
        print("=========================================")

makanan = Makanan()
minuman = Minuman()

while True:
    Menu.kop()
    Menu.menuJenis()
    
    pilih = int(input("\nMasukkan pilihan : "))
    
    if pilih == 1 :
        while True:
            Menu.kop()
            Menu.menuPengaturan()
            
            pilihan = int(input("\nMasukkan pilihan : "))
            
            if pilihan == 1 :
                while True:
                    Menu.kop()
                    print("\t \t>> Tambah Produk")
                    print("\t \t---------------------")
                    makanan.tambahProduk()
                    
                    choice = input("\nApakah Anda ingin menambah produk lagi? (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        break
            
            elif pilihan == 2 :
                while True:
                    Menu.kop()
                    print("\t \t>> Hapus Produk")
                    print("\t \t---------------------")
                    makanan.infoProduk()
                    makanan.hapusProduk()
                    
                    choice = input("\nApakah Anda ingin menghapus produk lagi? (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        break
            
            elif pilihan == 3 :
                while True:
                    Menu.kop()
                    print("\t \t>> Update Stok Produk")
                    print("\t \t---------------------")
                    makanan.infoProduk()
                    makanan.updateStokProduk()
                    
                    choice = input("\nApakah Anda ingin mengupdate stok produk lagi? (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        break
            
            elif pilihan == 4 :
                Menu.kop()
                print("\t \t>> Daftar Produk")
                print("\t \t---------------------")
                makanan.infoProduk()
                os.system('pause')
                
            elif pilihan == 0 :
                break
                
            else :
                print("Maaf pilihan ini tidak tersedia")
                continue
    
    elif pilih == 2 :
        while True:
            Menu.kop()
            Menu.menuPengaturan()
            
            pilihan = int(input("\nMasukkan pilihan : "))
            
            if pilihan == 1 :
                while True:
                    Menu.kop()
                    print("\t \t>> Tambah Produk")
                    print("\t \t---------------------")
                    minuman.tambahProduk()
                    
                    choice = input("\nApakah Anda ingin menambah produk lagi? (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        break
            
            elif pilihan == 2 :
                while True:
                    Menu.kop()
                    print("\t \t>> Hapus Produk")
                    print("\t \t---------------------")
                    minuman.infoProduk()
                    minuman.hapusProduk()
                    
                    choice = input("\nApakah Anda ingin menghapus produk lagi? (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        break
            
            elif pilihan == 3 :
                while True:
                    Menu.kop()
                    print("\t \t>> Update Stok Produk")
                    print("\t \t---------------------")
                    minuman.infoProduk()
                    minuman.updateStokProduk()
                    
                    choice = input("\nApakah Anda ingin mengupdate stok produk lagi? (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        break
            
            elif pilihan == 4 :
                Menu.kop()
                print("\t \t>> Daftar Produk")
                print("\t \t---------------------")
                minuman.infoProduk()
                os.system('pause')
            
            elif pilihan == 0 :
                break
            
            else :
                print("Maaf pilihan ini tidak tersedia")
                continue 
    
    elif pilih == 0 :
        exit(Menu.exit())
    
    else :
        print("Maaf pilihan ini tidak tersedia")
        continue

