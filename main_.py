
import numpy as np
import herni_pole

class Hra():

    hernipole = np.array(herni_pole.seznam_poli)

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
       
Hra.vypis()  
    

