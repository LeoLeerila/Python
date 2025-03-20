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

auto = Auto("ABC-123", 142)

auto.Kiihdyta(60)
auto.Kulje(1.5)
print(f"auton kuljettu matka on nyt: {auto.kuljettumatka}")