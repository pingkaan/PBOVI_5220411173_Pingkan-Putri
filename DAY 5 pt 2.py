#latihan

class Matkul:
    def __init__(self, mk1, mk2, mk3):
        self.mk1 = mk1
        self._mk2 = mk2
        self.__mk3 = mk3

class Tambahan(Matkul):
    def __init__(self, mk1, mk2, mk3, mk4):
        super().__init__(mk1, mk2, mk3)
        self.mk4 = mk4

data = Tambahan("PBO", "Sistem Operasi", "Basis Data", "PAD")
print("Mata kuliah hari ini:", data.mk1)
print("Mata kuliah hari ini:", data._mk2)
print("Mata kuliah hari ini:", data._Matkul__mk3)
print("Mata kuliah hari ini:", data.mk4)

# data("PBO", "Sistem Operasi", "Basis Data", "PAD")
# print("Perubahan ",data)