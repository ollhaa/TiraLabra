import random


class Markov:
    #Alustus
    def __init__(self):
        self.voittava = {0:"P", 1:"S", 2:"R"} # voittava valinta
        self.pisteet = {"R":{"R":0, "P":1, "S":0}, "P":{"R":0, "P":0, "S":1}, "S":{"R":1, "P":0, "S":0}} #pisteet valintojen perusteella eri Markoveille
       
    #Palauttaa tietokoneen vastauksen  
    def Answer(self, historia, edelliset, kierrokset, valinta):
        del kierrokset, valinta #poistetaan ne parametrit, joita ei käytetä tässä

        edelliset2 = edelliset[-2:] #edelliset kaksi pelaajan valintaa
        edelliset2 = "".join(edelliset2) #yhdistetään nämä merkkijonoksi

        apulista = historia[edelliset2] #muodostetaan apulista, jossa edellisen kahden frekfenssijakauma
        indeksi = apulista.index(max(apulista)) #suurin frekfenssi
        ans =  self.voittava[indeksi] #voittava valinta tähän suurimpaan frekfenssiin

        return ans
          
        

            
        