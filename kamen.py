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
    

kamen1_cerny = Kamen("cerny", "kamen1_cerny")
kamen2_cerny = Kamen("cerny", "kamen2_cerny")
kamen3_cerny = Kamen("cerny", "kamen3_cerny")
kamen4_cerny = Kamen("cerny", "kamen4_cerny")
kamen5_cerny = Kamen("cerny", "kamen5_cerny")
kamen6_cerny = Kamen("cerny", "kamen6_cerny")
kamen7_cerny = Kamen("cerny", "kamen7_cerny")
kamen8_cerny = Kamen("cerny", "kamen8_cerny")
kamen9_cerny = Kamen("cerny", "kamen9_cerny")
kamen10_cerny = Kamen("cerny", "kamen10_cerny")
kamen11_cerny = Kamen("cerny", "kamen11_cerny")
kamen12_cerny = Kamen("cerny", "kamen12_cerny")
kamen13_cerny = Kamen("cerny", "kamen13_cerny")
kamen14_cerny = Kamen("cerny", "kamen14_cerny")
kamen15_cerny = Kamen("cerny", "kamen15_cerny")

kamen1_bily = Kamen("bily","kamen1_bily")
kamen2_bily = Kamen("bily","kamen2_bily")
kamen3_bily = Kamen("bily","kamen3_bily")
kamen4_bily = Kamen("bily","kamen4_bily")
kamen5_bily = Kamen("bily","kamen5_bily")
kamen6_bily = Kamen("bily","kamen6_bily")
kamen7_bily = Kamen("bily","kamen7_bily")
kamen8_bily = Kamen("bily","kamen8_bily")
kamen9_bily = Kamen("bily","kamen9_bily")
kamen10_bily = Kamen("bily","kamen10_bily")
kamen11_bily = Kamen("bily","kamen11_bily")
kamen12_bily = Kamen("bily","kamen12_bily")
kamen13_bily = Kamen("bily","kamen13_bily")
kamen14_bily = Kamen("bily","kamen14_bily")
kamen15_bily = Kamen("bily","kamen15_bily")