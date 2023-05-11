from herni_pole import *


class Konzolovy_Hrac:
    def __init__(self,kamen):
        self.kamen = kamen

    def tah(self):
        Herni_pole.rozrad_kameny_do_poli()
        
        if self.kamen == "Bílý":
            hratelne_kameny = []
            for pole in seznam_poli:
                
                for kamen in pole:
                    
                    if kamen.barva == "bily":
                        hratelne_kameny.append(f"kamen: {kamen.nazev} pole: {Herni_pole.najdi_kamen(kamen)}")
            

            obsah_pole =  []
            pole_list = [pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10,pole11,pole12,pole13,pole14,pole15,pole16,pole17,pole18,pole19,pole20,pole21,pole22,pole23,pole24]
            for p in pole_list:
                obsah_pole.append(f"Pole{p.pole}: {[kamen.nazev for kamen in p.obsah_pole]}")


            print(f"Hratelné kameny a v jakých polích se nacházejí: {hratelne_kameny}")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"Všechna pole a jejich obsah: {obsah_pole}")
            k = input("S jakým hratelným kamenem chceš pohnout? Napiš název kamene: ")
            p = input("Na jaké pole ho chceš přesunout?: (1-24)")

        







        

        else:
            pass

class AI_Hrac:

    def __init__(self,kamen):
        self.kamen = kamen

    def tah(self):

        pass


seznam_poli = [pole1.obsah_pole, pole2.obsah_pole, pole3.obsah_pole, pole4.obsah_pole, pole5.obsah_pole, pole6.obsah_pole, pole7.obsah_pole, pole8.obsah_pole, pole9.obsah_pole, pole10.obsah_pole, pole11.obsah_pole, pole12.obsah_pole, pole13.obsah_pole, pole14.obsah_pole, pole15.obsah_pole, pole16.obsah_pole, pole17.obsah_pole, pole18.obsah_pole, pole19.obsah_pole, pole20.obsah_pole, pole21.obsah_pole, pole22.obsah_pole, pole23.obsah_pole, pole24.obsah_pole]



