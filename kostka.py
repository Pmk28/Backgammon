import random

class Kostka:
    def __init__(self, pocet_sten=6):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, self.pocet_sten)


class Dvojkostka(Kostka):
    def __init__(self):
        super().__init__()

    def hod_dvojice(self):
        x = self.hod()
        y = self.hod()
        if x != y:
          return (x , y)  
        else: 
            return ( x, x, x, x)
