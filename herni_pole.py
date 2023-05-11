from kamen import *


class Herni_pole:

    

    def __init__(self,pole):
        self.pole = pole
        self.obsah_pole = []
        
        
    def rozrad_kameny_do_poli():
        pole6.obsah_pole.extend([kamen1_cerny,kamen2_cerny,kamen3_cerny,kamen4_cerny,kamen5_cerny]) 
        pole8.obsah_pole.extend([kamen6_cerny,kamen7_cerny,kamen8_cerny])
        pole13.obsah_pole.extend([kamen9_cerny,kamen10_cerny,kamen11_cerny,kamen12_cerny,kamen13_cerny])
        pole24.obsah_pole.extend([kamen14_cerny,kamen15_cerny])
        pole1.obsah_pole.extend([kamen14_bily,kamen15_bily])
        pole12.obsah_pole.extend([kamen9_bily,kamen10_bily,kamen11_bily,kamen12_bily,kamen13_bily])
        pole17.obsah_pole.extend([kamen6_bily,kamen7_bily,kamen8_bily])
        pole19.obsah_pole.extend([kamen1_bily,kamen2_bily,kamen3_bily,kamen4_bily,kamen5_bily])
    def najdi_kamen(kamen):
       pole_list = [pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10,pole11,pole12,pole13,pole14,pole15,pole16,pole17,pole18,pole19,pole20,pole21,pole22,pole23,pole24]
       for p in pole_list:
            if kamen in p.obsah_pole:
                return p.pole
               
           
        
    



pole1 = Herni_pole(1)
pole2 = Herni_pole(2)
pole3 = Herni_pole(3)
pole4 = Herni_pole(4)
pole5 = Herni_pole(5)
pole6 = Herni_pole(6)


pole7 = Herni_pole(7)
pole8 = Herni_pole(8)
pole9 = Herni_pole(9)
pole10 = Herni_pole(10)
pole11 = Herni_pole(11)
pole12 = Herni_pole(12)

pole13 = Herni_pole(13)
pole14 = Herni_pole(14)
pole15 = Herni_pole(15)
pole16 = Herni_pole(16)
pole17 = Herni_pole(17)
pole18 = Herni_pole(18)

pole19 = Herni_pole(19)
pole20 = Herni_pole(20)
pole21 = Herni_pole(21)
pole22 = Herni_pole(22)
pole23 = Herni_pole(23)
pole24 = Herni_pole(24)

seznam_poli = [pole1.obsah_pole, pole2.obsah_pole, pole3.obsah_pole, pole4.obsah_pole, pole5.obsah_pole, pole6.obsah_pole, pole7.obsah_pole, pole8.obsah_pole, pole9.obsah_pole, pole10.obsah_pole, pole11.obsah_pole, pole12.obsah_pole, pole13.obsah_pole, pole14.obsah_pole, pole15.obsah_pole, pole16.obsah_pole, pole17.obsah_pole, pole18.obsah_pole, pole19.obsah_pole, pole20.obsah_pole, pole21.obsah_pole, pole22.obsah_pole, pole23.obsah_pole, pole24.obsah_pole]