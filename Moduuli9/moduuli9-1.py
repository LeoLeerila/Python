class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

auto = Auto("ABC-123", 142)

print(f"Auton rekisteri on {auto.rekisteri}, sen huippunopeus on {auto.huippunopeus}, sen nykyinen nopeus on {auto.nopeus} ja sen kuljettu matka on {auto.kuljettumatka}")