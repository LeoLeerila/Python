class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi
    
    def tulosta_tiedot(self):
        print(self.nimi)

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjoittaja {self.kirjoittaja}, sivumäärä {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittaja {self.paatoimittaja}")

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()