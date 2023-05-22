import numpy as np
import herni_pole
from hrac import *
from kostka import *
import time


class Hra():

    hernipole = np.array(herni_pole.seznam_poli)
    kostka = Kostka()
    hrac1 = None
    hrac2 = None

    def __init__(self):

        pass
        
    def start():
        Hra.vypis()
        Hra.prirazeni_hracu()
        hod = input("Zmáčkni mezerník a pak enter pro počáteční hod kostkou: ")
        if hod == " ":
            Hra.hody_kostkou()
        else:
            pass


    def vypis():
        print("-----------------------------------------------------")
        for i in range(16):
        
            print("|", end=' ')

            for row in Hra.hernipole[:13]:
            
                print(row[i], end=' ')

                if row[0] == "18" or row[0] == "BAR_C":
                    print("| |", end=' ')
        
           
        
            print("|")
        print("=====================================================")
        for n in range(16):
        
            print("|", end=' ')

            for row in Hra.hernipole[13:]:
            
                print(row[n], end=' ')

                if row[0] == "07" or row[0] == "BAR_B":
                    print("| |", end=' ')

            print("|")
        print("-----------------------------------------------------")
    def prirazeni_hracu():
        barva = input("Zmáčkni mezerník a pak enter pro výběr bílých kamenů nebo pouze enter pro výběr černých kamenů: ")
        if barva == " ":
            Hra.hrac1 = Konzolovy_Hrac("white")
            Hra.hrac2 = AI_Hrac("black")
            time.sleep(1)
            print("Hraješ tedy s bílými kameny a tvůj soupeř s černými!")
        else:
            Hra.hrac1 = Konzolovy_Hrac("black")
            Hra.hrac2 = AI_Hrac("white")
            print("Hraješ tedy s černými kameny a tvůj soupeř s bílými!")

    def hody_kostkou():
        x = Hra.kostka.hod()
        y = Hra.kostka.hod()
        print(f"Hodil si {x} a tvůj soupeř hodil {y}")
        if x > y:
            time.sleep(1)
            print("Začínáš s prvním tahem!")
            Hra.hrac1.tah()
        elif x == y:
            time.sleep(1)
            print("Hodili jste stejné číslo, házíte znovu!")
            time.sleep(1)
            Hra.hody_kostkou()
        else:
            time.sleep(1)
            print("Tvůj soupeř začíná s prvním tahem!")
            Hra.hrac2.tah()


     
    

        

Hra.start()



