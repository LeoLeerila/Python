class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def Kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

auto = Auto("ABC-123", 142)

auto.Kiihdyta(30)
auto.Kiihdyta(70)
auto.Kiihdyta(50)
print(f"Auton nykyinen nopeus: {auto.nopeus}")

auto.Kiihdyta(-200)
print(f"Auton nykyinen nopeus: {auto.nopeus}")