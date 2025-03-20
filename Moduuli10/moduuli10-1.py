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

hissi = Hissi()

hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(0)
