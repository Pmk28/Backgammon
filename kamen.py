class Kamen: 
    seznam = []   

    def __init__(self, barva,kamen_id):
        self._barva = barva
        self.pamet_pohybu = []  # Seznam polí, na kterých se kámen nacházel (včetně aktuálního)
        self.kamen_id = kamen_id
    
    @property 
    def barva(self):    
            return self._barva


    #Vrací aktuální pole, na kterém se kámen nachází.
    def get_pole(self):
        return self.pamet_pohybu[-1]
    
    def __str__(self):
        return f"kamen_{self.barva}{self.kamen_id}"


    #Vrací seznam polí, na kterých se kámen nacházel (včetně aktuálního).
    def get_pamet_pohybu(self):
        return self.pamet_pohybu
    
    def vytvor_kameny():
        for i in range(1,16):
            kamen_white = Kamen("white",i)
            Kamen.seznam.append(kamen_white)
        for i in range (1,16):
            kamen_black = Kamen("black",i)
            Kamen.seznam.append(kamen_black)

Kamen.vytvor_kameny()
