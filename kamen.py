class Kamen:    

    def __init__(self, barva, nazev):
        self.barva = barva
        self.pole = None  # Aktuální pole, na kterém se kámen nachází
        self.pamet_pohybu = []  # Seznam polí, na kterých se kámen nacházel (včetně aktuálního)
        self.nazev = nazev

    def get_barva(self):
        
        return self.barva

    def get_pole(self):
        """Vrací aktuální pole, na kterém se kámen nachází."""
        return self.pole

    def get_pamet_pohybu(self):
        """Vrací seznam polí, na kterých se kámen nacházel (včetně aktuálního)."""
        return self.pamet_pohybu
    

kamen1_cerny = Kamen("cerny", " C")
kamen2_cerny = Kamen("cerny", " C")
kamen3_cerny = Kamen("cerny", " C")
kamen4_cerny = Kamen("cerny", " C")
kamen5_cerny = Kamen("cerny", " C")
kamen6_cerny = Kamen("cerny", " C")
kamen7_cerny = Kamen("cerny", " C")
kamen8_cerny = Kamen("cerny", " C")
kamen9_cerny = Kamen("cerny", " C")
kamen10_cerny = Kamen("cerny", " C")
kamen11_cerny = Kamen("cerny", " C")
kamen12_cerny = Kamen("cerny", " C")
kamen13_cerny = Kamen("cerny", " C")
kamen14_cerny = Kamen("cerny", " C")
kamen15_cerny = Kamen("cerny", " C")

kamen1_bily = Kamen("bily"," B")
kamen2_bily = Kamen("bily"," B")
kamen3_bily = Kamen("bily"," B")
kamen4_bily = Kamen("bily"," B")
kamen5_bily = Kamen("bily"," B")
kamen6_bily = Kamen("bily"," B")
kamen7_bily = Kamen("bily"," B")
kamen8_bily = Kamen("bily"," B")
kamen9_bily = Kamen("bily"," B")
kamen10_bily = Kamen("bily"," B")
kamen11_bily = Kamen("bily"," B")
kamen12_bily = Kamen("bily"," B")
kamen13_bily = Kamen("bily"," B")
kamen14_bily = Kamen("bily"," B")
kamen15_bily = Kamen("bily"," B")