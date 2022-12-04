import Rps
class rpsApp:
#Alustus
    def __init__(self):
        self.peli = Rps.Rps()
        self.valinnatKokonimi = {"K": "Kivi", "P": "Paperi", "S":"Sakset"}
#vastustajan valinta
    def aloitusvalinnat(self):
        print("Valitse vastustaja! ")
        print("1 - Sari Satunnainen") #Satunnaisvalinta
        print("2 - Marko Markov(2)") #Toisen asteen Markov
        print("3 - Tekoäly") #Varsinainen tekoäly
#pelaajan valinnat pelissä
    def ohje(self):
        print("Vaihtoehdot:")
        print("K - Kivi ")
        print("P - Paperi ")
        print("S - Sakset ")
        print("Q - Lopetus ")

    def pelinPaattyminen(self):
        print("Peli on päättynyt!")
        yv = self.peli.yhteenveto()
        osuusPisteita = yv[3]/(yv[3]+yv[4])*100
        print(f"Pelatut kierrokset: {yv[5]}")
        print(f"Voittamasi kierrosten lukumäärä: {yv[3]}")
        print(f"{yv[6]}:n voittamien kierrosten lukumäärä: {yv[4]}")
        print(f"Sait annetuista pisteitä {osuusPisteita:.2f} %")

#pelin käynnistäminen
    def aloita(self):
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
            elif valinta =="K" or valinta =="P" or valinta =="S":
                self.peli.pelaa(valinta)
                #print(f"Valintasi oli: {valinta}")
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

