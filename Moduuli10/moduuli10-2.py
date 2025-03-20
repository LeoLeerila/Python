class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi())

    def aja_hissia(self, hissin_numero, kohdekerros):
        if kohdekerros > self.ylin_kerros:
            kohdekerros = self.ylin_kerros
        elif kohdekerros < self.alin_kerros:
            kohdekerros = self.alin_kerros
        self.hissit[hissin_numero-1].siirry_kerrokseen(kohdekerros)

class Hissi:
    def __init__(self):
        self.kerros = 0

    def kerros_ylos(self):
        self.kerros += 1
        print(f"hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"hissi on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kerrosmuutos):
        while kerrosmuutos > self.kerros:
            self.kerros_ylos()
        while kerrosmuutos < self.kerros:
            self.kerros_alas()

talo = Talo(-2, 10, 3)

talo.aja_hissia(1, -5)
talo.aja_hissia(3, 3)
talo.aja_hissia(2, 20)
