class Hewan:
    var1 = None #Public
    _var2 = None #Protected
    __var3 = None #Private

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    
    def __display(self):
        print("Ini menampilkan variabel private:", self.__var3)
    
    def akses(self):
        self.__display()

x = Hewan("Lion", "Octopus", "Dog")

#cara 1 memanggil hak akses modifier
print("Ini hewan pertama:", x.var1)
print("Ini hewan kedua:", x._var2)
print("Ini hewan ketiga:", x._Hewan__var3)

#cara 2 memanggil hak akses modifier
x.akses()



#INHERITANCE
class HewanDiLindungi(Hewan):
    def __init__(self, var1, var2, var3, var4):
        super().__init__(var1, var2, var3) #mengakses dengan kata kunci super()
        self.var4 = var4

y = HewanDiLindungi("Cendrawasih", "Anoa", "Badak Cula Satu", "Harimau Sumatra")
print("Hewan-hewan yang dilindungi:", y.var1, y._var2, y._Hewan__var3, y.var4)
