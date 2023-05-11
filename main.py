from kostka import *
from hrac import *
import time


class Hra:
    def __init__(self):
        self.play = None
        self.kostka = Kostka()
        
        

    def start(self):
        
        # print("Hraješ s bílými kameny")
        b = input("Vyber barvu kamenů se kterými budeš hrát - Napiš \"b\" pro bílé nebo \"c\" pro černé kameny: ")
        if b == "b":
            self.hrac1 = Konzolovy_Hrac('Bílý')
            self.hrac2 = AI_Hrac('Černý')
        elif b == "c":
            self.hrac1 = Konzolovy_Hrac('Černý')
            self.hrac2 = AI_Hrac('Bílý')
        else:
            print("Nevybral sis barvu kamene!")
            time.sleep(2)
            o = input("Chceš začít hrát znovu? - Napiš \"a\" pro ano nebo cokoliv jineho pro ne: ")
            if o == "a":
                hra1.start()
            else:
                pass
            

        self.hod_kostkou()

        

    def hod_kostkou(self):
        self.x = self.kostka.hod()
        self.z = self.kostka.hod()
        print(f"Hodil si číslo {self.x}")
        time.sleep(2)
        print(f"Tvůj soupeř hodil číslo {self.z}")
        
        if self.x > self.z:
            d = Dvojkostka()
            hd = d.hod_dvojice()
            print("Začínáš s prvním tahem")
            time.sleep(2)
            print(f"Hodil jsi čísla {hd[0]} a {hd[1]}")
            self.hrac1.tah()

        elif self.x == self.z:
            print("Hodili jste stejné číslo, házejte znovu")
            time.sleep(2)
            self.hod_kostkou()

        else:
            time.sleep(1)
            print("Tvůj soupeř začíná s prvním tahem")
            self.hrac1.tah()

        






Kostka1 = Kostka()
x = Kostka1.hod()
z = Kostka1.hod()

Dvojkostka1 = Dvojkostka()



hra1 = Hra()
hra1.start()



