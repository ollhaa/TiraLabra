import src.Rps as Rps
class rpsApp:

    def __init__(self):
        self.peli = Rps.Rps()

    def aloitusvalinnat(self):
        print("Valitse vastustaja! ")
        print("1 - Rose Random")
        print("2 - Mark Markov(2)")
        print("3 - Multi AI")

    def ohje(self):
        print("Vaihtoehdot:")
        print("R - Rock ")
        print("P - Paper ")
        print("S - Scissors ")
        print("Q - Lopetus ")

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
            if valinta =="Q":
                break
            elif valinta =="R" or valinta =="P" or valinta =="S":
                self.peli.pelaa(valinta)
                tilanne = self.peli.yhteenveto()
                print(f"Valintasi: {valinta}")
                yv = self.peli.yhteenveto()
                print(f"Valintasi oli: {yv[0]}, Pistetilanne: (sinä:) {yv[1]} - (tietokone:) {yv[2]} Pelattuja kierroksia: {yv[3]}")

            else:

                print("Et valinnut mitään")
                

if __name__ == "__main__":
    uusi = rpsApp()
    uusi.aloita()
