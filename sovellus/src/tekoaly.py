import random

class Tekoaly:
    '''
    Luokka, joka pelaa pelin varsinaista tekoälyä. Yhteensä seitsemän eri tapaa pelata:
    0. Satunnainen
    1.-3. Markov-ketjut pituudella 1-3
    4. Palauttaa valinnan, joka olisi voittava valinta tietokoneen edelliseen valintaan
    5. Palauttaa pelaajan edellisen kierroksen valinnan
    6. Palauttaa valinnan, joka on voittava valinta siihen, jonka pelaamisesta on pisin aika

    Attributes:
        pelattava: pelattavista tekoälyistä valittu - aluksi satunnaisvalinta
        tilastot: lista, jossa listoja eri tekoälyjen valinnat
        tulokset: lista, jossa pisteet eri tekoälyjen valinnoille
        voittava: sanakirja, joka "palauttaa" voittavat valinnat tiettyyn valintaan
        pisteet: sanakirja, joka "palauttaa" saadut pisteet tietylle valinnalle
        muutos: muuttaa valinnan str -> int (käytetään apuna)
    '''

    def __init__(self):
        '''
        Luokan kontsruktori.
        '''
        self.pelattava = 0
        self.tilastot = [[] for x in range(7)]
        self.tulokset = [[] for x in range(7)]
        self.voittava = {0:["P", "C"], 1:["S", "L"], 2:["K", "C"], 3:["K", "S"], 4:["P","L"]}
        self.pisteet = {"K":{"K":0, "P":1, "S":-1, "L":-1, "C":1}, "P":{"K":-1, "P":0, "S":1, "L":1, "C":-1},
        "S":{"K":1, "P":-1, "S":0, "L":-1, "C":1}, "L":{"K":1, "P":-1, "S":1, "L":0, "C":-1},
        "C":{"K":-1, "P":1, "S":-1, "L":1, "C":0}}
        self.muutos  ={"K":0, "P":1, "S":2, "L":3, "C":4}

    def set_pelattava(self, pelattava:int):
        '''
        Testausta varten, jotta voidaan asettaa haluttu vaihtoehto pelattavaksi algoritmiksi

        Arguments:
            pelattava: annetaan numero, joka asettaa pelattavan algoritmin. 0 on satunnainen jne.
        '''
        self.pelattava = pelattava

    def get_pelattava(self):
        '''
        testausta varten luotu. Palauttaa self.pelattavan.
        '''
        return self.pelattava

    def answer(self, historia:dict, edelliset:list, kierrokset:int, valinta:str):
        '''
        Palauttaa tietokoneen vastauksen ja tallentaa optimointia algoritmin valinnat ja pisteet

        Args:
            historia: Sanakirja, jossa tehdyt valinnat ja seurannut valintojen frekvenssilista.
            edelliset: Pelaajan edelliset valinnat listana.
            kierrokset: Kierrosten lkm.
            valinta: Pelaajan edellinen valinta.

        Returns:
            Palauttaa palautettava, joka on tietokoneen valinta pelissä.
        '''
        for i in range(7):
            if i ==0:
                ans = random.choice(["K", "P", "S", "L", "C"])
            elif i < 4:
                edelliset_n = edelliset[-i:]
                edelliset_n = "".join(edelliset_n)
                apulista = historia[edelliset_n]
                indeksi = random.choices(["K","P","S","L","C"], weights = apulista)
                apu = self.muutos[indeksi[0]]
                ans =  random.choice(self.voittava[apu])
            elif i ==4:
                if len(self.tilastot[self.pelattava]) ==0:
                    ans = random.choices(["K", "P", "S", "L", "C"])
                else:
                    apu = self.tilastot[self.pelattava][-1]
                    apu2 = self.muutos[apu]
                    ans = random.choice(self.voittava[apu2])
            elif i ==5:
                if len(edelliset) ==0:
                    apu = random.choices(["K", "P", "S", "L", "C"])
                    ans = apu[0]
                else:
                    ans = edelliset[-1]
            else:
                def pisin_aika(pelatut_valinnat):
                    '''
                    Apufunktio, joka ratkaisee valinnan, jonka pelaamisesta pelaajalla on pisin aika

                    Args:
                        pelatutValinnat: Pelaajan aiemmin pelatut valinnat

                    Returns:
                        kasitellyt[-1], joka valinta, jonka pelaamisesta pisin aika
                    '''
                    kasitellyt =[]
                    kasitellyt.append(pelatut_valinnat[-1])
                    for x in range(len(pelatut_valinnat)):
                        if len(kasitellyt) ==3:
                            break
                        elif pelatut_valinnat[-x] in kasitellyt:
                            continue
                        else:
                            kasitellyt.append(pelatut_valinnat[-x])

                    return kasitellyt[-1]

                apu = pisin_aika(edelliset)
                apu2 = self.muutos[apu]
                ans = random.choice(self.voittava[apu2])

            piste = self.pisteet[valinta][ans]
            self.tulokset[i].append(piste)
            self.tilastot[i].append(ans)

        palautettava = self.tilastot[self.pelattava][-1]

        #7 kierroksen välein vertailu algoritmien välillä ja valitaan paras (edelliset 7 kierrosta)
        if kierrokset % 7 ==0:
            summalista = [sum(x[-7:]) for x in self.tulokset]
            index = summalista.index(max(summalista))
            self.pelattava = index
        return palautettava
