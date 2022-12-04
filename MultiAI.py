import random
#Luokan on tarkoitus olla "se lopullinen tekoäly"

class MultiAI:
    def __init__(self):
        self.pelattava = 0 #pelattavista tekoälyistä valittu - aluksi satunnaisvalinta
        self.tilastot = [[] for x in range(6)] #luodaan lista, jossa listoja eri tekoälyjen valinnat
        self.tulokset = [[] for x in range(6)] #luodaan lista, jossa pisteet eri tekoälyjen valinnoille
        self.voittava = {0:"P", 1:"S", 2:"K"} # voittava valinta. Esim 0= R -> P voittava
        self.pisteet = {"K":{"K":0, "P":1, "S":-1}, "P":{"K":-1, "P":0, "S":1}, "S":{"K":1, "P":-1, "S":0}} #pisteet valintojen perusteella eri tekoälyille
        self.muutos  ={"K":0, "P":1, "S":2} #apu muutoksia varten

    #Answer palauttaa tekoälyn vastauksen
    def Answer(self, historia, edelliset, kierrokset, valinta): 
        #print(f"pelattava: {self.pelattava}")
        
        for i in range(6): #pelataan eri tekoälyt jokaisella kierroksella
            if i ==0:
                ans = random.choice(["K", "P", "S"]) #1. satunnainen valinta
            elif i < 4: #Markov-ketjut pituuksilla 1-3
                edelliset_n = edelliset[-i:]
                edelliset_n = "".join(edelliset_n)
                apulista = historia[edelliset_n] 
                indeksi = apulista.index(max(apulista))
                ans =  self.voittava[indeksi]  
            elif i ==4: #pelattavan tekoälyn viimeisen valinnan voittava valinta
                apu = self.tilastot[self.pelattava][-1]
                #print(f"apu: {apu}")
                apu2 = self.muutos[apu]
                ans = self.voittava[apu2]
            else: #valinta joka voittaa, jos pelaaja pelaa sitä valintaa jonka pelaamisesta pisin aika
                def pisinAika(pelatutValinnat):
                    print(f"pelatut valinnat: {pelatutValinnat}")
                    #pisinAika2 =pelatutValinnat[-1]
                    kasitellyt =[]
                    kasitellyt.append(pelatutValinnat[-1])
                    for x in range(len(pelatutValinnat)):
                        if len(kasitellyt) ==3:
                            #pisinAika2 = kasitellyt[-1]
                            break
                        elif pelatutValinnat[-x] in kasitellyt:
                            continue
                        else:
                            kasitellyt.append(pelatutValinnat[-x])

                    return kasitellyt[-1]

                apu = pisinAika(edelliset)
                apu2 = self.muutos[apu]
                ans = self.voittava[apu2]
            
            self.tulokset[i].append(self.pisteet[valinta][ans])
            self.tilastot[i].append(ans)

        palautettava = self.tilastot[self.pelattava][-1]

        #optimoidaan seitsemän kierroksen välein pelattava tekoäly
        if kierrokset % 7 ==0:
            summalista = [sum(x) for x in self.tulokset[-7:]]
            print(self.pelattava)
            index = summalista.index(max(summalista))
            self.pelattava = index
            print(self.pelattava)
            #self.tilastot = [[] for x in range(6)]
        
        
        return palautettava
