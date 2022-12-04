import random
import Markov as Markov
import MultiAI as MultiAI

#alustus
class Rps:
    def __init__(self):
        self.nimi =""
        self.pelaajanValinnat = []
        self.tietokoneenValinnat = []
        self.pelatutKierrokset = 0
        self.pelaajanVoitto = False
        self.vaihtoehdot = ["K", "P", "S"]
        self.historia = {}
        self.pelaajanPisteet =0
        self.tietokoneenPisteet =0
        self.markov = None

#luonti ja historia
    def alusta(self, vastustaja:str):
        if vastustaja == "1":
            self.nimi = "Sari Satunnainen"
        elif vastustaja =="2":
            self.nimi="Marko Markov2"
            self.markov = Markov.Markov()
        else:
            self.nimi = "Tekoäly"
            self.markov= MultiAI.MultiAI()
        
        def create(n):
            if n ==1:
                return ["K", "P", "S"]
            else:
                return [x + sana for x in ["K", "P", "S"] for sana in create(n-1)]

        permutaatiot =[]
        for i in range(1,4):
            permutaatiot += create(i)
        
        for i in range(len(permutaatiot)):
            self.historia[permutaatiot[i]] = [0,0,0]

    def getNimi(self):
        return self.nimi

    def getPelaajanPisteet(self):
        return self.pelaaja

    def getTietokoneenPisteet(self):
        return self.tietokone
#pelin eteneminen
    def pelaa(self, valinta):  
        self.pelatutKierrokset +=1

        if self.pelatutKierrokset <5 or self.nimi =="Sari Satunnainen":
            vastaus = random.choice(self.vaihtoehdot)
        else: 
            vastaus = self.markov.Answer(self.historia, self.pelaajanValinnat, self.pelatutKierrokset, valinta)

        if self.pelatutKierrokset >=3:
            size = 3 
        else: 
            size = self.pelatutKierrokset

        edelliset_3 = self.pelaajanValinnat[-size:]
        #print(f"edelliset3: {edelliset_3}")

        def solver(lista, n, valinta):
            for i in range(0,len(lista)):
                b= lista[i:n]
                b= "".join(b)
                print(f"b: {b}")
                indeksi = {"K":0, "P":1, "S":2}
                muutos = indeksi[valinta]
                apulista = self.historia[b] #TÄMÄ!
                #print(f"apulista: {apulista}")
                apulista[muutos] +=1
                self.historia[b] = apulista
        
        #MUOKKAA SOLVERIN AVULLA SELF.HISTORIAA!
        solver(edelliset_3,size, valinta)        
        #print(self.historia)

        self.pelaajanValinnat.append(valinta)
        self.tietokoneenValinnat.append(vastaus)

        if (valinta =="K" and vastaus == "P") or (valinta =="P" and vastaus == "S") or (valinta =="S" and vastaus == "K"):
            self.pelaajanVoitto = False
            self.tietokoneenPisteet +=1
        elif valinta == vastaus:
            self.pelaajanVoitto = None
        else:
            self.pelaajanVoitto =True
            self.pelaajanPisteet +=1
#palauttaa käyttöliittymälle tietoja pelistä
    def yhteenveto(self):
        a = self.pelaajanValinnat[-1]
        b = self.tietokoneenValinnat[-1]
        c = self.pelaajanVoitto
        d = self.pelaajanPisteet
        e = self.tietokoneenPisteet
        f = self.pelatutKierrokset
        g = self.nimi
        
        return (a,b,c,d,e,f,g)


