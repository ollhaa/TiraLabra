import random
import Markov as Markov
import MultiAI as MultiAI

class Rps:
    '''Luokka, jossa varsinainen pelilogiikka on.

    Attributes:
        nimi: Tietokoneen vastustajan nimi. Tämä määräytyy pelaajan vastustajavalinnan perusteella. 
        pelaajanValinnat: Pelaajan tehdyt valinnat
        tietokoneetValinnat: Tietokoneen pelaamat valinnat
        pelatutKierrokset: Pelattujen kierrosten lkm
        pelaajanVoitto: Päättyikö kierros pelaajan voittoon
        vaihtoehdot: Vaihtoehdot, joita pelissä voi pelata
        historia: 1-3 siirron historiaan perustuva frekvenssilista. Eli mikä on seurannut esim. "PP" jälkeen. Listan frekvenssit järjestyksessä K-P-S
        pelaajanPisteet: Pelaajan pisteet pelissä
        tietokoneenPisteet: Tietokoneen pisteet pelissä.
        markov: Pelaajan valitessa vastustajaksi "Marko Markov2" tai "Tekoäly" markoviksi asetetaan tuotu luokka Markov tai MultiAI.
    '''
    def __init__(self):
        '''Luokan konstruktori, joka luo pelilogiikan.
  
        '''
        self.nimi =""
        self.pelaajanValinnat = []
        self.tietokoneenValinnat = []
        self.pelatutKierrokset = 0
        self.pelaajanVoitto = False
        self.vaihtoehdot = ["K", "P", "S", "L", "C"]
        self.voittavatValinnat = {"K":["S", "L"], "P":["K", "C"], "S":["P", "L"], "L":["P", "C"], "C":["K", "S"]}
        self.historia = {}
        self.pelaajanPisteet =0
        self.tietokoneenPisteet =0
        self.markov = None

    def alusta(self, vastustaja:str):
        '''Asettaa vastustajan ja luo historiaan listat frekvensseille (tapahtuu sisäisen create-funktion avulla).

        Args:
            vastustaja: Nimeksi tulee valittu vastustaja
        '''
        if vastustaja == "1":
            self.nimi = "Sari Satunnainen"
        elif vastustaja =="2":
            self.nimi="Marko Markov2"
            self.markov = Markov.Markov()
        else:
            self.nimi = "Tekoäly"
            self.markov= MultiAI.MultiAI()
        
        def create(n:int):
            '''alusta-metodin sisäinen funktio luo historiaan listat frekvensseille

            Args:
                n: Markov-ketjun pituuteen liittyvä parametri.

            Returns: 
                listan, jossa pelattuvien vaihtoehtojen yhdistelmät
            '''
            if n ==1:
                return ["K", "P", "S", "L", "C"]
            else:
                return [x + sana for x in ["K", "P", "S", "L", "C"] for sana in create(n-1)]

        permutaatiot =[]
        for i in range(1,4):
            permutaatiot += create(i)
        
        for i in range(len(permutaatiot)):
            self.historia[permutaatiot[i]] = [0,0,0,0,0]

    def pelaa(self, valinta: str):
        '''Pelin varsinainen logiikka on tässä. Lisää kierrosten määrän, palauttaa tietokoneen vastauksen ja muokkaa historiaa. 

        Args:
            valinta: Pelaajan antama valinta 
        ''' 
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

        def solver(lista: list, n:int, valinta:str):
            '''Pelaa-metodin sisäinen funktio. Muokkaa historiaa pelaajan edellisten valintojen ja nykyisen valinnan perusteella.

            Args:
                lista: Annetut edelliset valinnat. 
                n: Edellisten valintojen määrä
                valinta: Pelaajan valinta
            '''
            for i in range(0,len(lista)):
                b = lista[i:n]
                b = "".join(b)
                indeksi = {"K":0, "P":1, "S":2, "L":3, "C":4}
                muutos = indeksi[valinta]
                apulista = self.historia[b]
                apulista[muutos] +=1
                self.historia[b] = apulista
        

        solver(edelliset_3,size, valinta)        

        self.pelaajanValinnat.append(valinta)
        self.tietokoneenValinnat.append(vastaus)


        if vastaus == valinta:
            self.pelaajanVoitto = None
        elif vastaus not in self.voittavatValinnat[valinta]: 
            self.pelaajanVoitto = False
            self.tietokoneenPisteet +=1
        else:
            self.pelaajanVoitto =True
            self.pelaajanPisteet +=1

    def yhteenveto(self):
        '''Palauttaa yhteenvedon pelistä

        Returns:
            Palauttaa seuraavat asiat tupplena:
            a = Pelaajan viimeinen valinta
            b = Tietokoneen viimeinen valinta
            c = True, jos kierros päättyi pelaajan voittoo, False, jos tietokoneen voittoon ja muuuten None (=tasapeli)
            d = Pelaajan pisteet pelissä
            e = Tietokoneen pisteet pelissä
            f = Pelatut kierrokset yhteensä pelissä
            g = Vastustajan eli tietokoneen nimi
        '''
        a = self.pelaajanValinnat[-1]
        b = self.tietokoneenValinnat[-1]
        c = self.pelaajanVoitto
        d = self.pelaajanPisteet
        e = self.tietokoneenPisteet
        f = self.pelatutKierrokset
        g = self.nimi
        
        return (a,b,c,d,e,f,g)


