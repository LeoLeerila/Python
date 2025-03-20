class Hissi:
    def __init__(self):
        self.alin = 0
        self.ylin = 10
        self.kerros = self.alin

    def kerros_ylos(self):
        self.kerros += 1
        print(f"hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"hissi on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kerrosmuutos):
        if kerrosmuutos > self.ylin:
            kerrosmuutos = self.ylin
        elif kerrosmuutos < self.alin:
            kerrosmuutos = self.alin
        while kerrosmuutos > self.kerros:
            self.kerros_ylos()
        while kerrosmuutos < self.kerros:
            self.kerros_alas()

hissi = Hissi()

hissi.siirry_kerrokseen(11)
hissi.siirry_kerrokseen(-1)
