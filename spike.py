from kamen import Kamen

class Spike:
    seznam = []

    def __init__(self, spike_id):
        self._spike_barvy = None
        self._kameny = []
        self.spike_id = spike_id

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
    
    def __str__(self):
        return f"spike_{self.spike_id}"

    
    
    def vytvorit():
        for i in range(1,25):
             spike_i = Spike(i)
             Spike.seznam.append(spike_i)
             
             


