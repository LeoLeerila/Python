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

class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasitetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasitetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, tankinkoko):
        super().__init__(rekisteri, huippunopeus)
        self.tankinkoko = tankinkoko

sahko = Sahkoauto("ABC-15", 180, 52.5)
polttomoottori = Polttomoottoriauto("ACD-123", 165, 32.3)

sahko.Kiihdyta(100)
polttomoottori.Kiihdyta(150)
sahko.Kulje(3)
polttomoottori.Kulje(3)

print(f"Sähköauton kulkema matka {sahko.kuljettumatka}\nPolttomoottoriauton kulkema matka {polttomoottori.kuljettumatka}")