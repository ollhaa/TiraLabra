import random
#Luokan on tarkoitus olla "se lopullinen tekoäly" - vielä hieman kesken. 

class MultiAI:
    def __init__(self):
        self.pelattava = 0 # 
        self.tilastot = [[] for x in range(6)]
        self.voittava = {0:"P", 1:"S", 2:"R"} # voittava valinta
        self.pisteet = {"R":{"R":0, "P":1, "S":-1}, "P":{"R":-1, "P":0, "S":1}, "S":{"R":1, "P":-1, "S":0}} #pisteet valintojen perusteella eri tekoälyille

    def Answer(self, historia, edelliset, nimi, kierrokset, valinta):
        
        for i in range(6):
            if i ==0:
                ans = random.choice(["R", "P", "S"])
            elif i < 4:
                edelliset = edelliset[-i:]
                apulista = historia[edelliset] 
                indeksi = apulista.index(max(apulista))
                ans =  self.voittava[indeksi]
            else:
                ans = self.tilastot.edelliset[-1]
            
            self.tilastot[i].append(ans)

        if kierrokset % 5 ==0:
            summalista = [sum(x) for x in self.tilastot]
            index = summalista.index(max(summalista))
            self.pelattava = index
            self.tilastot = [[] for x in range(6)]
        
        
        return self.tilastot[self.pelattava][-1]
