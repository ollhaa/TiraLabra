import random


class Markov:
    def __init__(self):
        self.mpituus = 1 #Ketjun pituus
        self.yksi = ["R", "P", "S", "R", "P"] # valinnat aluksi
        self.kaksi = ["P", "S", "R", "P", "S"]
        self.kolme = ["S", "R", "P","R", "P"]
        self.voittava = {0:"P", 1:"S", 2:"R"} # voittva valinta
        self.pisteet = {"R":{"R":0, "P":1, "S":0}, "P":{"R":0, "P":0, "S":1}, "S":{"R":1, "P":0, "S":0}} #pisteet valintojen perusteella eri Markoveille
       

    def Answer(self, historia, edelliset, nimi, kierrokset, valinta):
        def Markov1(edelliset1, historia):
                apulista = historia[edelliset1] 
                indeksi = apulista.index(max(apulista))
                ans =  self.voittava[indeksi]
                self.yksi.append(ans)
                return ans

        def Markov2(edelliset2, historia):
                apulista = historia[edelliset2]
                indeksi = apulista.index(max(apulista))
                ans =  self.voittava[indeksi]
                self.kaksi.append(ans)
                return ans

        def Markov3(edelliset3, historia):
                apulista = historia[edelliset3]
                indeksi = apulista.index(max(apulista))
                ans =  self.voittava[indeksi]
                self.kolme.append(ans)
                return ans
          
        if nimi == "Mark Markov2": #Jos vastustaja Mark Markov2 niin pelataan vaan Markov(2)
            edelliset2 = edelliset[-2:]
            edelliset2 = "".join(edelliset2)
            ans =  Markov2(edelliset2, historia)
            return ans


        else: # Muulloin pelataan kaikki kolme ja valitaan seuravaille kierroksille "paras"
            if kierrokset % 5 ==0:
                n1 = n2 = n3 = 0
                self.yksi = self.yksi[-5:]
                self.kaksi = self.kaksi[-5:]
                self.kolme = self.kolme[-5:]

                for i in range(0,4):
                    n1 += self.pisteet[edelliset[i]][self.yksi[i]]
                    n2 += self.pisteet[edelliset[i]][self.kaksi[i]]
                    n3 += self.pisteet[edelliset[i]][self.kolme[i]]
                n1 += self.pisteet[valinta][self.yksi[-1]]
                n2 += self.pisteet[valinta][self.kaksi[-1]]
                n3 += self.pisteet[valinta][self.kolme[-1]]

                self.mpituus = [n1, n2, n3].index(max(n1,n2,n3)) +1 # Tämä ei onnistu?
                print(f"self.pituus :{self.mpituus}") 
                self.yksi.clear()
                self.kaksi.clear() 
                self.kolme.clear()


            edelliset1 = edelliset[-1:]
            edelliset1 = "".join(edelliset1)
            a = Markov1(edelliset1, historia)
            #print(f"a: {a}")
            self.yksi.append(a)
            print(f"yksi: {self.yksi}")

            edelliset2 = edelliset[-2:]
            edelliset2 = "".join(edelliset2)
            b = Markov2(edelliset2, historia)
            self.kaksi.append(b)
            #print(f"kaksi: {self.kaksi}")

            edelliset3 = edelliset[-3:]
            edelliset3 = "".join(edelliset3)
            c = Markov3(edelliset3, historia)
            self.kolme.append(c)
        
        if self.mpituus ==1: return a
        elif self.mpituus ==2: return b
        else: return c 
            
        