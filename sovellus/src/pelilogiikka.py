import random
import time
from markov import Markov
from tekoaly import Tekoaly

class Pelilogiikka:
    '''
    Luokka, jossa varsinainen pelilogiikka on.

    Attributes:
        nimi: Valitun vastustajan nimi. Määräytyy pelaajan alkuvalinnan perusteella.
        pelaajan_valinnat: Pelaajan tehdyt valinnat
        tietokoneet_valinnat: Tietokoneen pelaamat valinnat
        pelatut_kierrokset: Pelattujen kierrosten lkm
        pelaajan_voitto: Päättyikö kierros pelaajan voittoon
        vaihtoehdot: Vaihtoehdot, joita pelissä voi pelata
        historia: 1-3 siirron historiaan perustuva frekvenssilista.
        Listan frekvenssit järjestyksessä K-P-S-L-C
        pelaajan_pisteet: Pelaajan pisteet pelissä
        tietokoneen_pisteet: Tietokoneen pisteet pelissä.
        markov: Pelaajan valitsema vastustajaluokka
        yhteis_aika: pitää yllä pelaa-funktion "käyttämää" aikaa
    '''
    def __init__(self):
        '''
        Luokan konstruktori, joka luo pelilogiikan.
        '''
        self.nimi =""
        self.pelaajan_valinnat = []
        self.tietokoneen_valinnat = []
        self.pelatut_kierrokset = 0
        self.pelaajan_voitto = False
        self.vaihtoehdot = ["K", "P", "S", "L", "C"]
        self.voittavat_valinnat = {"K":["S", "L"], "P":["K", "C"], "S":["P", "L"],
        "L":["P", "C"], "C":["K", "S"]}
        self.historia = {}
        self.pelaajan_pisteet =0
        self.tietokoneen_pisteet =0
        self.markov = None
        self.yhteis_aika =0

    def alusta(self, vastustaja : str):
        '''
        Asettaa vastustajan ja luo historiaan listat frekvensseille
        (tapahtuu sisäisen create-funktion avulla).

        Args:
            vastustaja: Nimeksi tulee valittu vastustaja
        '''
        if vastustaja == "1":
            self.nimi = "Sari Satunnainen"
        elif vastustaja == "2":
            self.nimi = "Marko Markov2"
            self.markov = Markov()
        else:
            self.nimi="Tekoäly"
            self.markov=Tekoaly()
        def create(n_pituus: int):
            '''
            alusta-metodin sisäinen funktio luo historiaan listat frekvensseille

            Args:
                n_pituus: Markov-ketjun pituuteen liittyvä parametri.

            Returns:
                listan, jossa pelattuvien vaihtoehtojen yhdistelmät
            '''
            if n_pituus ==1:
                return ["K", "P", "S", "L", "C"]
            return [x + sana for x in ["K", "P", "S", "L", "C"] for sana in create(n_pituus-1)]

        permutaatiot =[]
        for i in range(1,4):
            permutaatiot += create(i)
        for i in range(len(permutaatiot)):
            self.historia[permutaatiot[i]] = [1,1,1,1,1]

    def pelaa(self, valinta: str):
        '''
        Pelin varsinainen logiikka.

        Args:
            valinta: Pelaajan antama valinta
        '''
        alkuaika=time.time()
        self.pelatut_kierrokset +=1
        if self.pelatut_kierrokset <7 or self.nimi == "Sari Satunnainen":
            vastaus = random.choice(self.vaihtoehdot)
        else:
            vastaus = self.markov.answer(self.historia, self.pelaajan_valinnat, self.pelatut_kierrokset, valinta)
        if self.pelatut_kierrokset >=3:
            size = 3
        else:
            size = self.pelatut_kierrokset
        edelliset_3 = self.pelaajan_valinnat[-size:]
        def tallentaja(lista: list, n:int, valinta:str):
            '''
            Pelaa-metodin sisäinen funktio. Muokkaa historiaa pelaajan edellisten valintojen
            ja nykyisen valinnan perusteella.

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
        tallentaja(edelliset_3,size, valinta)
        self.pelaajan_valinnat.append(valinta)
        self.tietokoneen_valinnat.append(vastaus)
        if vastaus == valinta:
            self.pelaajan_voitto = None
        elif vastaus not in self.voittavat_valinnat[valinta]:
            self.pelaajan_voitto = False
            self.tietokoneen_pisteet +=1
        else:
            self.pelaajan_voitto =True
            self.pelaajan_pisteet +=1

        loppuaika = time.time()
        kulunut_aika = loppuaika - alkuaika
        self.yhteis_aika += kulunut_aika

    def get_kierrokset(self):
        '''
        Palauttaa pelatut kierrokset

        Returns:
            pelattujen kierrosten lkm
        '''
        return self.pelatut_kierrokset

    def yhteenveto(self):
        '''
        Palauttaa yhteenvedon pelistä

        Returns:
            Palauttaa seuraavat asiat tupplena:
            a = Pelaajan viimeinen valinta
            b = Tietokoneen viimeinen valinta
            c = True, jos kierros päättyi pelaajan voittoo, muuten False/None
            d = Pelaajan pisteet pelissä
            e = Tietokoneen pisteet pelissä
            f = Pelatut kierrokset yhteensä pelissä
            g = Vastustajan eli tietokoneen nimi
            h = pelilogiikan aika
        '''
        a = self.pelaajan_valinnat[-1]
        b = self.tietokoneen_valinnat[-1]
        c = self.pelaajan_voitto
        d = self.pelaajan_pisteet
        e = self.tietokoneen_pisteet
        f = self.pelatut_kierrokset
        g = self.nimi
        h = self.yhteis_aika
        return (a,b,c,d,e,f,g,h)
