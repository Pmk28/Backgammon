from spike import *
from bar import *
from kostka import *
import time


class Konzolovy_Hrac:

    def __init__(self,kamen):
        
        self.kamen = kamen
        self.x = None
        

    def tah_2(self):
        pole = int(input("Napiš číslo pole: "))
        kamen = int(input("Napiš číslo kamene: "))
        for sutr in Spike.seznam[pole - 1].kameny:
            
            if self.kamen == "white" and sutr.barva == "white":
                pass
            elif self.kamen == "black" and sutr.barva == "black":
                pass
            else:
                pass

        


                

        


        
    def tah_4(self):

        pass
    
    def vyhod_z_baru(self):
        

        pass

    def hod_dvojkostkou(self):
        dvojkostka = Dvojkostka()
        hod = input("Zmáčkni mezerník a pak enter pro hod dvojicí kostek: ")
        self.x = dvojkostka.hod_dvojice() 
        if hod == " ":
            if len(self.x) == 2:
                print(f"Hodil si čísla {self.x[0]} a {self.x[1]}!")
                self.tah_2()
            else:
                print(f"Hodil si čísla {self.x[0]} a {self.x[1]}!")
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






