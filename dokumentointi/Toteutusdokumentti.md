# Toteutusdokumentti

### Ohjelman yleisrakenne
Ohjelma koostuu käyttöliittymäluokasta (RpsApp), varsinaisesta ohjelemasta (Rps), Markov-luokasta (Markov) ja luokasta, jossa varsinainen tekoäly on (MultiAI).

Ohjelma käynnistyy luokasta RpsApp, jossa ensin kysytään haluttu vastustaja. Vaihtoehtoja vastustajaksi ovat:
 - **Sari Satunnainen**, jossa tietokone pelaa satunnaisvalintaa.
 - **Marko Markov2**, jossa tietokone pelaa toisen asteen Markov-ketjua perustuen pelaajan valintoihin.
 - **Tekoäly**, jossa tietokone pelaa kuutta eri tekoälyä, joista valitaan aina paras edellisten seitsemän kierroksen perusteella jokin pelaamaan seuraaville seitsemälle kierrokselle.

Tämän jälkeen käynnistyy varsinainen peli. Pelissä annetaan valinta, ja saadaan tämän jälkeen takaisin tietokoneen valinta. Lisäksi saadaan luokasta Rps palautuarvona mm. pelaajan pisteet, kierrokset yms., joiden perusteella voidaan kertoa peliä pelaavalle tilanne pelistä. Kun pelaaja päättää pelin lopetuskomennolla, niin muodostetaan yhteenveto lopputilanteesta. 

Varsinainen pelin logiikka toteutetaan luokassa Rps. Kun peli luodaan, niin pelille muodostuu mm. oliomuuttujiksi historia, kierrosten lukumäärä ja tietokoneen tekoäly (self.markov). Tämän jälkeen alustetaan peli pelaajan käyttöliittymässä annetuilla valinnoilla osa näistä oli muuttujista (mm. nimi ja pelattava tekoäly/tekoälyluokka, joka palauttaa valinnat). 
Peli eteneminen tapahtuu metodin "pelaa", avulla. Jos vastustajaksi on valittu: 
 - **"Sari Satunnainen"**, niin vastaus on satunnaisvalinta annetuista siirroista.
 - **"Marko Markov2"**, niin self.markoviksi on asetettu luokka Markov. Tällöin Answer palauttaa kahteen viimeiseen siirtoo perustuvan valinnan.
 - **"Tekoäly"** palauttaa vastauksen MultiAI-luokasta, jossa taustalla pelataan kuutta eri algoritmia. Tällöin self.markoviksi on asetettu luokka MultiAI.
 
Markov-luokassa palautetaan siis vastaus perustuen kahteen viimeiseen valintaan. Markov-luokan Answer-metodille annetaan syötteena pelissä mm. pelin historia ja edellisen valinnat, jotta algoritmi voidaan toteuttaa. Historia on toteutettu sanakirjana, jossa eri mittaisille (1-3) yhdistelmille (esim. "KPS" muodostuu lista tätä yhdistelmää seuraavan valinnan frekvensseistä. Esim. [0,3,1], jossa järjestys K-P-S - eli yleisin on P). 
Koska tämä luokka ei vaadi kierrosten lukumäärätietoa tai pelattua valintaa, niin poistetaan alussa nämä. Nämä ovat siksi, että Answer toimii myös luokassa MultiAI, jossa niitä tarvitaan. Eli molempien luokkien metodi on sama, mutta pelattava (perustuen palaajan alussa antamaan valintaan) asetetaan self.markoviksi alussa.
MultiAI-luokka on pelin varsinainen tekoäly. Kun luokka luodaan, niin olioparametreiksi tulee mm. lista listoista, joiden avulla eri algoritmien menetysttä voidaan seurata. Tätäkin käytetään (kuten yllä on mainittu) Answer-metodin kautta. Nyt tarvitaan kaikki parametrit, koska mm. kierrosten lukumäärätieto tarvitaan MultiAI-luokan palauttaman algoritmin valintaan. Eli pelataan taustalla kaikki kuusi algoritmia, mutta "paras" palauttaa vastauksen peliin.  Luokassa pelattavat kuusi algoritmia ovat:
 - **Satunnaisvalinta.**
 - **Markov-ketjut pituuksilla 1-3.**
 - **Pelattavan algoritmin viimeisen valinnan voittava algoritmi.**
 - **Algoritmi, joka palauttaa voittavan siirron sille valinnalle, jonka pelaamisesta on pisin aika.**
 



### Saavutetut aika- ja tilavaativuudet
### Suorituskyky- ja O-analyysivertailu 
### Työn mahdolliset puutteet ja parannusehdotukset
