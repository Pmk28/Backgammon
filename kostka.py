import random

class Kostka:
    def __init__(self, pocet_sten=6):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, self.pocet_sten)


class Dvojkostka(Kostka):
    def hod_dvojice(self):
        return (self.hod(), self.hod())

    def hod_ctverice(self):
        return (self.hod(), self.hod(), self.hod(), self.hod())

