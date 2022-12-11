import random

class MultiAI:
    '''Luokka, joka pelaa pelin varsinaista tekoälyä. Yhteensä kuusi eri tapaa pelata:
    0.. Satuinnainen
    1.-3. Markov-ketjut pituudella 1-3
    4. Palauttaa valinnan, joka olisi voittava valinta tietokoneen edelliseen valintaan
    5. Palauttaa valinnan, joka on voittava valinta siihen, jonka pelaamisesta on pisin aika

    Attributes:
        pelattava: pelattavista tekoälyistä valittu - aluksi satunnaisvalinta
        tilastot: lista, jossa listoja eri tekoälyjen valinnat
        tulokset: lista, jossa pisteet eri tekoälyjen valinnoille
        voittava: sanakirja, joka "palauttaa" voittavat valinnat tiettyyn valintaan
        pisteet: sanakirja, joka "palauttaa" saadut pisteet tietylle valinnalle 
        muutos 
    '''

    def __init__(self):
        '''Luokan kontsruktori. 
        '''
        self.pelattava = 0 
        self.tilastot = [[] for x in range(6)] 
        self.tulokset = [[] for x in range(6)] 
        self.voittava = {0:["P", "C"], 1:["S", "L"], 2:["K", "C"], 3:["K", "S"], 4:["P","L"]} 
        self.pisteet = {"K":{"K":0, "P":1, "S":-1, "L":-1, "C":1}, "P":{"K":-1, "P":0, "S":1, "L":1, "C":-1}, "S":{"K":1, "P":-1, "S":0, "L":-1, "C":1}, "L":{"K":1, "P":-1, "S":1, "L":0, "C":-1}, "C":{"K":-1, "P":1, "S":-1, "L":1, "C":0}} 
        self.muutos  ={"K":0, "P":1, "S":2, "L":3, "C":4} 

    def Answer(self, historia, edelliset, kierrokset, valinta): 
        '''Palauttaa tietokoneen vastauksen.

        Args:
            historia: Sanakirja, josta nähdään tehdyt valinnat ja näitä seurannut valintojen frekvenssilista.
            edelliset: Pelaajan edelliset valinnat listana.
            kierrokset: Kierrosten lkm.
            valinta: Pelaajan edellinen valinta.

        Returns:
            Palauttaa ans, joka on tietokoneen valinta pelissä.
        '''
        for i in range(6): 
            if i ==0:
                ans = random.choice(["K", "P", "S", "L", "C"]) 
            elif i < 4: 
                edelliset_n = edelliset[-i:]
                edelliset_n = "".join(edelliset_n)
                apulista = historia[edelliset_n] 
                indeksi = apulista.index(max(apulista))
                ans =  random.choice(self.voittava[indeksi])  
            elif i ==4: 
                apu = self.tilastot[self.pelattava][-1]
                apu2 = self.muutos[apu]
                ans = random.choice(self.voittava[apu2])
            else: 
                def pisinAika(pelatutValinnat):
                    '''Apufunktio, joka ratkaisee valinnan, jonka pelaamisesta pelaajalla on pisin aika

                    Args: 
                        pelatutValinnat: Pelaajan aiemmin pelatut valinnat

                    Returns:
                        kasitellyt[-1], joka valinta, jonka pelaamisesta pisin aika 
                    '''
                    kasitellyt =[]
                    kasitellyt.append(pelatutValinnat[-1])
                    for x in range(len(pelatutValinnat)):
                        if len(kasitellyt) ==3:
                            break
                        elif pelatutValinnat[-x] in kasitellyt:
                            continue
                        else:
                            kasitellyt.append(pelatutValinnat[-x])

                    return kasitellyt[-1]

                apu = pisinAika(edelliset)
                apu2 = self.muutos[apu]
                ans = random.choice(self.voittava[apu2])
            
            self.tulokset[i].append(self.pisteet[valinta][ans])
            self.tilastot[i].append(ans)

        palautettava = self.tilastot[self.pelattava][-1]

        #Seitsemän kierroksen välein tehdään vertailua eri algoritmien välillä ja valitaan se, joka on ollut paras edellisellä seitsemällä kierroksella
        if kierrokset % 7 ==0:
            summalista = [sum(x) for x in self.tulokset[-7:]]
            index = summalista.index(max(summalista))
            self.pelattava = index
            
        return palautettava
