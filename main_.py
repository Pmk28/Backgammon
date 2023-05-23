import numpy as np
import herni_pole
from hrac import *
from kostka import *
import time


class Hra():

    def __init__(self):

        self.hrac1 = None
        self.hrac2 = None

        self.herni_pole = np.array(herni_pole.seznam_poli)
        self.kostka = Kostka()
        
    def start(self):
        Spike.vytvorit()
        Kamen.vytvor_kameny()
        hra.vypis()
        hra.prirazeni_hracu()
        hod = input("Zmáčkni mezerník a pak enter pro počáteční hod kostkou: ")
        if hod == " ":
            hra.hody_kostkou()
        else:
            pass


    def vypis(self):
        print("-----------------------------------------------------")
        for i in range(16):
        
            print("|", end=' ')

            for row in self.herni_pole[:13]:
            
                print(row[i], end=' ')

                if row[0] == "18" or row[0] == "BAR_C":
                    print("| |", end=' ')
        
           
        
            print("|")
        print("=====================================================")
        for n in range(16):
        
            print("|", end=' ')

            for row in self.herni_pole[13:]:
            
                print(row[n], end=' ')

                if row[0] == "07" or row[0] == "BAR_B":
                    print("| |", end=' ')

            print("|")
        print("-----------------------------------------------------")
    def prirazeni_hracu(self):
        barva = input("Zmáčkni mezerník a pak enter pro výběr bílých kamenů nebo pouze enter pro výběr černých kamenů: ")
        if barva == " ":
            self.hrac1 = Konzolovy_Hrac("white")
            self.hrac2 = AI_Hrac("black")
            time.sleep(1)
            print("Hraješ tedy s bílými kameny a tvůj soupeř s černými!")
        else:
            self.hrac1 = Konzolovy_Hrac("black")
            self.hrac2 = AI_Hrac("white")
            print("Hraješ tedy s černými kameny a tvůj soupeř s bílými!")

    def hody_kostkou(self):
        x = self.kostka.hod()
        y = self.kostka.hod()
        print(f"Hodil si {x} a tvůj soupeř hodil {y}")
        if x > y:
            time.sleep(1)
            print("Začínáš s prvním tahem!")
            self.hrac1.hod_dvojkostkou()
        elif x == y:
            time.sleep(1)
            print("Hodili jste stejné číslo, házíte znovu!")
            time.sleep(1)
            self.hody_kostkou()
        else:
            time.sleep(1)
            print("Tvůj soupeř začíná s prvním tahem!")
            self.hrac2.tah()


     
    

        
hra = Hra()
hra.start()



