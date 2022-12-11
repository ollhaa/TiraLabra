import Rps
class rpsApp:
    '''Luokka, joka toimii käyttöliittymänä varsinaiselle pelille.

    Attributes:
        peli: Laajennettu KPS tuodaan pelattavaksi peliksi
        valinnatKokonimi: Sanakirjan avulla muodostetaan sallituista syötteistä valintojen koko nimet.
    '''
    def __init__(self):
        '''Luokan konstruktori, joka luo käyttöliittymänä varsinaiselle pelille.
        '''
        self.peli = Rps.Rps()
        self.valinnatKokonimi = {"K": "Kivi", "P": "Paperi", "S":"Sakset", "L":"Lisko", "C":"SpoCk"}


    def aloitusvalinnat(self):
        '''Tulostaa peliä aloittaessa valinnat pelin vastustajaksi.
        '''
        print("Valitse vastustaja! ")
        print("1 - Sari Satunnainen") 
        print("2 - Marko Markov(2)") 
        print("3 - Tekoäly") 


    def ohje(self):
        '''Tulostaa pelissä jokaiselle kierrokselle vaihtoehdot pelissä. 
        '''
        print("Vaihtoehdot:")
        print("K - Kivi")
        print("P - Paperi")
        print("S - Sakset")
        print("L - Lisko")
        print("C - SpoCk")
        print()
        print("Q - Lopetus ")


    def pelinPaattyminen(self):
        '''Pelin päätyessä tulostaa yhteenvedon pelistä-
        '''
        print("Peli on päättynyt!")
        yv = self.peli.yhteenveto()
        osuusPisteita = yv[3]/(yv[3]+yv[4])*100
        print(f"Pelatut kierrokset: {yv[5]}")
        print(f"Voittamasi kierrosten lukumäärä: {yv[3]}")
        print(f"{yv[6]}:n voittamien kierrosten lukumäärä: {yv[4]}")
        print(f"Sait annetuista pisteitä {osuusPisteita:.2f} %")


    def aloita(self):
        '''Aloittaa varsinaisen pelin käyttöliittymän while-silmukassa. Ensin valitaan vastustaja ja sitten peli alkaa.
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
                self.pelinPaattyminen()
                break
            elif valinta =="K" or valinta =="P" or valinta =="S" or valinta =="L" or valinta == "C":
                self.peli.pelaa(valinta)
                yv = self.peli.yhteenveto()
                print(f"Valintasi oli: {self.valinnatKokonimi[yv[0]]} ja tietokoneen valinta oli {self.valinnatKokonimi[yv[1]]}...") 
                if yv[2]: print("...Voitit!")
                elif yv[2]==False: print("...Hävisit!") 
                else: print("...Tasapeli") 
                print(f"Pistetilanne: Sinä: {yv[3]} - {yv[6]}: {yv[4]}. Pelattuja kierroksia nyt: {yv[5]}")
            else:
                print("Et valinnut mitään")
                

if __name__ == "__main__":
    uusi = rpsApp()
    uusi.aloita()

