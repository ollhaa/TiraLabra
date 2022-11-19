import random
from collections import deque 
import Markov as Markov


class Rps:
    def __init__(self):
        self.nimi =""
        self.tehdyt_valinnat = []
        self.tk_valinnat = []
        self.kierrokset = 0
        self.voitto = False
        self.vaihtoehdot = ["R", "P", "S"]
        self.historia = {}
        self.pelaaja =0
        self.tietokone =0
        #self.markov = None

    def alusta(self, vastustaja:str):
        if vastustaja == "1":
            self.nimi = "Rose Random"
        elif vastustaja =="2":
            self.nimi="Mark Markov2"
            #self.markov = Markov.Markov()
        else:
            self.nimi = "Multi Markov"
            #self.markov= Markov.Markov()
        
        def create(n):
            if n ==1:
                return ["R", "P", "S"]
            else:
                return [x + sana for x in ["R", "P", "S"] for sana in create(n-1)]

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

    def pelaa(self, valinta):
        
        self.kierrokset +=1

        if self.kierrokset <5 or self.nimi =="Rose Random":
            vastaus = random.choice(self.vaihtoehdot)
        else: 
            vastaus = Markov.Markov().Answer(self.historia, self.tehdyt_valinnat, self.nimi, self.kierrokset, valinta)

        if self.kierrokset >=3:
            size = 3 
        else: 
            size = self.kierrokset

        edelliset_3 = self.tehdyt_valinnat[-size:]
        #print(f"edelliset3: {edelliset_3}")

        def solver(lista, n, valinta):
            for i in range(0,len(lista)):
                b= lista[i:n]
                b= "".join(b)
                print(f"b: {b}")
                indeksi = {"R":0, "P":1, "S":2}
                muutos = indeksi[valinta]
                apulista = self.historia[b] #TÄMÄ!
                #print(f"apulista: {apulista}")
                apulista[muutos] +=1
                self.historia[b] = apulista
        
        #MUOKKAA SOLVERIN AVULLA SELF.HISTORIAA!
        solver(edelliset_3,size, valinta)        
        #print(self.historia)

        self.tehdyt_valinnat.append(valinta)

        if (valinta =="R" and vastaus == "P") or (valinta =="P" and vastaus == "S") or (valinta =="S" and vastaus == "R"):
            self.voitto = False
            self.tietokone +=1
        elif valinta == vastaus:
            self.voitto = None
        else:
            self.voitto =True
            self.pelaaja +=1

    def yhteenveto(self):
        a = self.voitto
        b = self.pelaaja
        c = self.tietokone
        d = self.kierrokset
        
        return (a,b,c,d)


