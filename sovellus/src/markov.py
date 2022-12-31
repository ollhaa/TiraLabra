import random

class Markov:
    '''
    Luokka, joka pelaa "Marko Markov2" -vastustajaa. Tässä kahden asteen Markov-ketju.

    Attributes:
        voittava: Sanakirja, joka palauttaa valinnat, jotka voittavat annetun valinnan.
        0=K, 1=P, 2=S, 3=L ja 4=C.
        Kiven voittavat valinnat ovat P ja C.
        muutos: muuttaa str -> int (käytetään apuna)
    '''
    def __init__(self):
        '''
        Luokan konstruktori, joka luo uuden Markovin.
        '''
        self.voittava = {0:["P", "C"], 1:["S", "L"], 2:["K", "C"], 3:["K", "S"], 4:["P","L"]}
        self.muutos = {"K":0, "P":1, "S":2, "L":3, "C":4}

    def answer(self, historia:dict, edelliset:list, kierrokset:int, valinta:str):
        '''
        Palauttaa tietokoneen vastauksen.

        Args:
            historia: Sanakirja, jossa tehdyt valinnat ja valintojen frekvenssilista.
            edelliset: Pelaajan edelliset valinnat listana.
            kierrokset: Kierrosten lkm. Poistetaan tässä luokassa.
            valinta: Pelaajan edellinen valinta.

        Returns:
            Palauttaa ans, joka on tietokoneen valinta pelissä.
        '''
        del kierrokset, valinta

        edelliset2 = edelliset[-2:]
        edelliset2 = "".join(edelliset2)
        apulista = historia[edelliset2]
        indeksi = random.choices(["K","P","S","L","C"], weights = apulista)

        apu = self.muutos[indeksi[0]]
        ans =  random.choice(self.voittava[apu])

        return ans
