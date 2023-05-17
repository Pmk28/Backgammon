from kamen import Kamen

class Spike:
    def __init__(self, spike_id):
        self._spike_barvy = None
        self._kameny = []

    @property
    def kameny(self):
        return self._kameny
    def pridej_kamen(self,spike_id, Kamen):
        self._kameny.append(Kamen)

    def pocet_kamenu(self, spike_id):
        return len(self._kameny)

    def je_prazdny(self, spike_id):
        return len(self._kameny) == 0

    def odeber_kamen(self, spike_id, Kamen):
        self._kameny.remove(Kamen)
        print("Kamen je pryč")
        
