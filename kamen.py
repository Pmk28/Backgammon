class Kamen:    

    def __init__(self, barva, nazev):
        self._barva = barva
        self.pamet_pohybu = []  # Seznam polí, na kterých se kámen nacházel (včetně aktuálního)
        self._nazev = nazev
    
    @property 
    def barva(self):    
            return self._barva


    #Vrací aktuální pole, na kterém se kámen nachází.
    def get_pole(self):
        return self.pamet_pohybu[-1]


    #Vrací seznam polí, na kterých se kámen nacházel (včetně aktuálního).
    def get_pamet_pohybu(self):
        return self.pamet_pohybu
