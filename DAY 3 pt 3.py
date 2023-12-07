class Coba :
    def __init__(self, x2, x3):
        self.xx1 = 5
        self.xx2 = x2
        self.xx3 = x3
    
    def terbesar(self, a, b, c):
        if self.xx1 > b and self.xx1 > c :
            max = a
        elif b > a and b > c :
            max = b
        elif c > self.xx1 and c > b :
            max = c
        return max

nil2 = 9
nil3 = 10

bidang = Coba(nil2,nil3)

print("Angka terbesar ", bidang.terbesar(bidang.xx1, nil2, nil3))