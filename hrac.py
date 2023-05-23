from spike import *
from bar import *
from kostka import *
import time


class Konzolovy_Hrac:

    def __init__(self,kamen):
        
        self.kamen = kamen
        

    def tah_2(self):
        
        pass


        
    def tah_4(self):

        pass
    
    def vyhod_z_baru(self):
        

        pass

    def hod_dvojkostkou(self):
        dvojkostka = Dvojkostka()
        hod = input("Zmáčkni mezerník a pak enter pro hod dvojicí kostek: ")
        if hod == " ":
            if len(dvojkostka.hod_dvojice()) == 2:
                print(f"Hodil si čísla {dvojkostka.hod_dvojice()[0]} a {dvojkostka.hod_dvojice()[1]}!")
                self.tah_2()
            else:
                print(f"Hodil si čísla {dvojkostka.hod_dvojice()[0]} a {dvojkostka.hod_dvojice()[1]}!")
                time.sleep(1)
                print("Hodil si 2 stejná čísla, můžeš tedy táhnout čtyřikrát!")
                self.tah_4()
        else:
            pass
        

        







        

class AI_Hrac:

    def __init__(self,kamen):
        self.kamen = kamen

    def tah(self):
        dvojkostka = Dvojkostka()
        pass
        
    def vyhod_z_baru(self):
        pass






