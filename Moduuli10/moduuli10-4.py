import random

class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, osallistuvat_autot):
        self.nimi = kilpailun_nimi
        self.pituus = kilpailun_pituus
        self.autolista = osallistuvat_autot

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.Kiihdyta(random.randint(-10, 15))
            auto.Kulje(1)
    
    def tulosta_tilanne(self):
        print(f"{self.nimi}\nrekisteri, kuljettu matka, nopeus, huippunopeus")
        for auto in self.autolista:
            print(f"{auto.rekisteri}, {auto.kuljettumatka}, {auto.nopeus}, {auto.huippunopeus}")
    
    def kilpailu_ohi(self):
        onko_ohi = False
        for auto in self.autolista:
            if auto.kuljettumatka >= self.pituus:
                onko_ohi = True
        return onko_ohi

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

kilpailu = Kilpailu("Suuri romuralli", 8000, autolista)

#nollataan autolista ettei sitä kaytetä vahingossa
autolista = 0

#aloitetaan kilpailu
kilpailutunti = 0
while kilpailu.kilpailu_ohi() == False:
    kilpailu.tunti_kuluu()
    kilpailutunti += 1
    if kilpailutunti == 10:
        kilpailutunti = 0
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()