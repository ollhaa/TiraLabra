from pelilogiikka import Pelilogiikka

class PeliApp:
    '''
    Luokka, joka toimii käyttöliittymänä varsinaiselle pelille.
    Attributes:
        peli: Pelilogiikka tuodaan pelattavaksi peliksi
        valinnat_kokonimi: Sanakirjan avulla syötteistä valintojen koko nimet.
    '''
    def __init__(self):
        '''Luokan konstruktori, joka toimii käyttöliittymänä varsinaiselle pelille.
        '''
        self.peli = Pelilogiikka()
        self.valinnat_kokonimi = {"K": "Kivi", "P": "Paperi", "S":"Sakset", "L":"Lisko", "C":"SpoCk"}

    def aloitusvalinnat(self):
        '''
        Tulostaa peliä aloittaessa valinnat pelin vastustajaksi.
        '''
        print("Valitse vastustaja! ")
        print("1 - Sari Satunnainen")
        print("2 - Marko Markov(2)")
        print("3 - Tekoäly")

    def ohje(self):
        '''
        Tulostaa pelissä jokaiselle kierrokselle vaihtoehdot pelissä.
        '''
        print("Vaihtoehdot:")
        print("K - Kivi")
        print("P - Paperi")
        print("S - Sakset")
        print("L - Lisko")
        print("C - SpoCk")
        print("")
        print("Q - Lopetus")

    def pelin_paattyminen(self):
        '''
        Pelin päätyessä tulostaa yhteenvedon pelistä
        '''
        print("")
        print("Peli on päättynyt!")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        kierrokset = self.peli.get_kierrokset()
        if kierrokset ==0:
            print("Et pelannut kierrostakaan!")
        else:
            yv = self.peli.yhteenveto()
            osuus_pisteita = yv[3]/(yv[3]+yv[4])*100
            print(f"Pelatut kierrokset: {yv[5]}")
            print(f"Voittamasi kierrosten lukumäärä: {yv[3]}")
            print(f"{yv[6]}:n voittamien kierrosten lukumäärä: {yv[4]}")
            print(f"Sait annetuista pisteitä {osuus_pisteita:.2f} %")
            print(f"Pelaa-funktion keskimääräinen aika: {yv[7]/ yv[5]} sekuntia")
            print("")

    def aloita(self):
        '''
        Aloittaa varsinaisen pelin käyttöliittymän. Ensin valitaan vastustaja ja aloitus.
        '''
        while True:
            self.aloitusvalinnat()
            vastustaja = input()
            print("")
            if vastustaja == "1" or vastustaja == "2" or vastustaja == "3":
                self.peli.alusta(vastustaja)
                break

        while True:
            print("")
            self.ohje()
            valinta = input("Anna valinta: \n")
            valinta = valinta.capitalize()
            if valinta =="Q":
                self.pelin_paattyminen()
                break
            elif valinta =="K" or valinta =="P" or valinta =="S" or valinta =="L" or valinta == "C":
                self.peli.pelaa(valinta)
                yv = self.peli.yhteenveto()
                print(f"Valintasi oli: {self.valinnat_kokonimi[yv[0]]} ja tietokoneen valinta oli {self.valinnat_kokonimi[yv[1]]}...")
                if yv[2]:
                    print("...Voitit!")
                elif yv[2] is False:
                    print("...Hävisit!")
                else: print("...Tasapeli")
                print(f"Pistetilanne: Sinä: {yv[3]} - {yv[6]}: {yv[4]}. Pelattuja kierroksia nyt: {yv[5]}")
            else:
                print("Et valinnut mitään")

uusi = PeliApp()
uusi.aloita()
