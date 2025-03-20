import random

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
    
    def Kulje(self, aika):
        self.kuljettumatka += self.nopeus * aika

autolista = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    autolista.append(Auto(("ABC-" + str(i)), huippunopeus))

print("Kilpailevat autot")
for auto in autolista:
    print(auto.rekisteri)

voittaja = 0
while voittaja == 0:
    for auto in autolista:
        if auto.kuljettumatka >= 10000:
            voittaja = 1
        else:
            auto.Kiihdyta(random.randint(-10, 15))
            auto.Kulje(1)

print("rekisteri, kuljettu matka, nopeus, huippunopeus")
for auto in autolista:
    print(f"{auto.rekisteri}, {auto.kuljettumatka}, {auto.nopeus}, {auto.huippunopeus}")