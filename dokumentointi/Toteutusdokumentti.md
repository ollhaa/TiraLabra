# Toteutusdokumentti

### Ohjelman yleisrakenne ja toiminta
Ohjelma koostuu käyttöliittymäluokasta (peliApp), varsinaisesta ohjelmasta (pelilogiikka), Markov-luokasta (Markov) ja luokasta, jossa varsinainen tekoäly on (Tekoaly).

Ohjelma käynnistyy luokasta peliApp, jossa ensin kysytään haluttu vastustaja. Vaihtoehtoja vastustajaksi ovat:
 - **Sari Satunnainen**, jossa tietokone pelaa satunnaisvalintaa.
 - **Marko Markov2**, jossa tietokone pelaa toisen asteen Markov-ketjua perustuen pelaajan valintoihin.
 - **Tekoäly**, jossa tietokone pelaa seitsemää eri tekoälyä, joista valitaan aina paras edellisten seitsemän kierroksen perusteella jokin pelaamaan seuraaville seitsemälle kierrokselle.

Tämän jälkeen käynnistyy varsinainen peli. Pelissä annetaan valinta, ja saadaan tämän jälkeen takaisin tietokoneen valinta. Lisäksi saadaan luokasta pelilogiikka palautuarvona mm. pelaajan pisteet, kierrokset yms., joiden perusteella voidaan kertoa peliä pelaavalle tilanne pelistä. Kun pelaaja päättää pelin lopetuskomennolla, niin muodostetaan yhteenveto lopputilanteesta. 

Varsinainen pelin logiikka toteutetaan luokassa pelilogiikka. Kun peli luodaan, niin pelille muodostuu mm. oliomuuttujiksi historia, kierrosten lukumäärä ja tietokoneen tekoäly (self.markov). Tämän jälkeen alustetaan peli pelaajan käyttöliittymässä annetuilla valinnoilla osa näistä oli muuttujista (mm. nimi ja pelattava tekoäly/tekoälyluokka, joka palauttaa valinnat). 

Peli eteneminen tapahtuu metodin "pelaa", avulla. Jos vastustajaksi on valittu: 
 - **"Sari Satunnainen"**, niin vastaus on satunnaisvalinta annetuista siirroista.
 - **"Marko Markov2"**, niin self.markoviksi on asetettu luokka Markov. Tällöin Answer palauttaa kahteen viimeiseen siirtoo perustuvan valinnan.
 - **"Tekoäly"** palauttaa vastauksen Tekoaly-luokasta, jossa taustalla pelataan seitsemää eri algoritmia. Tällöin self.markoviksi on asetettu luokan Tekoaly-olio.
 
### Operaatioiden toteutus

Markov-luokassa palautetaan siis vastaus perustuen kahteen viimeiseen valintaan. Markov-luokan Answer-metodille annetaan syötteena pelissä mm. pelin historia ja edellisen valinnat, jotta algoritmi voidaan toteuttaa. Historia on toteutettu sanakirjana, jossa eri mittaisille (1-3) yhdistelmille (esim. "KPS" muodostuu lista tätä yhdistelmää seuraavan valinnan frekvensseistä. Esim. [1,3,1,1,1], jossa järjestys K-P-S-L-C. Edellisen listan todennäköisyydet ovat [1/7, 3/7, 1/7, 1/7, 1/7] ja näistä arvontaan tietokoneen valinta näillä todennäköisyyksillä. Frekvenssit on alustettu listana [1,1,1,1,1], jollon aluksi kaikkien valintojen todennäköisyys on 0.2.  

Koska Markov-luokka ei vaadi kierrosten lukumäärätietoa tai pelattua valintaa, niin poistetaan alussa nämä. Nämä ovat siksi, että Answer toimii myös luokassa MultiAI, jossa niitä tarvitaan. Eli molempien luokkien metodi on sama, mutta pelattava (perustuen palaajan alussa antamaan valintaan) asetetaan self.markoviksi alussa.
Tekoaly-luokka on pelin varsinainen tekoäly. Kun luokka luodaan, niin olioparametreiksi tulee mm. lista listoista, joiden avulla eri algoritmien menetysttä voidaan seurata. Tätäkin käytetään (kuten yllä on mainittu) Answer-metodin kautta. Nyt tarvitaan kaikki parametrit, koska mm. kierrosten lukumäärätieto tarvitaan MultiAI-luokan palauttaman algoritmin valintaan. Eli pelataan taustalla kaikki seitsemän algoritmia, mutta "paras" palauttaa vastauksen peliin.  Luokassa pelattavat seitsemän algoritmia ovat:
 - **Satunnaisvalinta.**
 - **Markov-ketjut pituuksilla 1-3.**
 - **Pelattavan algoritmin viimeisen valinnan voittava algoritmi.**
 - **Algoritmi, joka palauttaa pelaajan viimeisen valinnan**
 - **Algoritmi, joka palauttaa voittavan siirron sille valinnalle, jonka pelaamisesta on pisin aika.**
 

### Suorituskyky


### Työn mahdolliset puutteet ja parannusehdotukset

Luokassa tekoäly voisi olla vieläkin useampia vaihtoehtoja, joita pelata. Sovellukseen olisi voinut tehdä myös graafisen käyttöliittymän. Sovelluksessa  olisi voinut olla vielä enemmän testausta ja koodia hieman selvempää.
