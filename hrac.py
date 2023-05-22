from spike import *
from bar import *
from kostka import *


class Konzolovy_Hrac:

    def __init__(self,kamen):
        
        self.kamen = kamen
        

    def tah(self):
        dvojkostka = Dvojkostka()
        hod = input("Zmáčkni mezerník a pak enter pro hod dvojicí kostek: ")
        if hod == " ":
            if len(dvojkostka.hod_dvojice()) == 2:
                pole = int(input("Napiš číslo pole: "))
                kamen = int(input("Napiš číslo kamene se kterým chceš pohnout(číslování od 0 odshora dolů): "))
                tah = int(input(f"{dvojkostka.hod_dvojice()[0]}, {dvojkostka.hod_dvojice()[1]}"))
                if tah in  [i for i in range(1,7)]:
                    for i in Spike.seznam[pole].kameny:
                        if i == kamen:
                            pass
                else:
                    pass
            else:
                pass
        else:
            pass
        


        
        
    
    def vyhod_z_baru(self):
        

        pass
            

        







        

class AI_Hrac:

    def __init__(self,kamen):
        self.kamen = kamen

    def tah(self):
        dvojkostka = Dvojkostka()
        pass
        
    def vyhod_z_baru(self):
        pass






