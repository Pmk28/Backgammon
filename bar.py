from kamen import Kamen

class Bar:
    def __init__(self, bar_barvy):
        self.bar_barvy = bar_barvy
        self.kameny = []

    def pridej_kamen(self, barva):
        if barva not in self.bar_barvy:
            raise ValueError(f"Bar neobsahuje kameny barvy {barva}")
        self.kameny.append(Kamen(barva, None))

    def pocet_kamenu(self):
        return len(self.kameny)

    def je_prazdny(self):
        return len(self.kameny) == 0

bily = Bar("bily")
cerny = Bar("cerny")
