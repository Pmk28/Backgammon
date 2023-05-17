from kamen import Kamen

class Spike:
    def __init__(self, spike_id):
        self.spike_barvy = spike_barvy
        self.kameny = []

    def pridej_kamen(self,spike_id, Kamen):
        self.kameny.append(Kamen)

    def pocet_kamenu(self, spike_id):
        return len(self.kameny)

    def je_prazdny(self, spike_id):
        return len(self.kameny) == 0
    def odeber_kamen(self, spike_id, Kamen):
        self.kameny.remove(Kamen)
        print("Kamen je pryč")
        
