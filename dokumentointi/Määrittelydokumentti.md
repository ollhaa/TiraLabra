# Määrittelydokumentti
---
### Aihe
Laajennetun Kivi-Paperit-Sakset -peli, jossa mukana myös Lisko ja Spock*. Tarkoituksena on luoda vastustajaksi tekoäly, joka pelaa pelaajaa vastaan. Tekoälyn haasteena on kaksi asiaa:

* Miten tietokone löytää säännönmukaisuuksia ihmisen pelitavasta?
* Miten tietokone sopeutuu, jos pelaaja muuttaa tapaansa pelata?

Luon siis peli, jossa on mahdollista pelata kolmea vastustajaa vastaan, joista tekoäly on tämän kurssin kannalta olennaisin. Tekoäly pelaa useampaa stretegiaa taustalla, ja valitsee säännöllisin väliajoin edellisten kierrosten perusteella sen algoritmin, jota pelataan seuraavat kierrokset. 

*Laajennetun pelin säännöt löytyvät dokumentin lopusta.

### Valitut algoritmit ja tietorakenteet
Eräs tapa löytää säännönmukaisuuksia ihmisen pelitavasta on Markov-ketjut. Markov-ketjussa uusi tila riippuu vain edellisestä tilasta. Mikäli pelaajalla on taipumis pelata tietyn valinnan (esim. "kivi") jälkeen aina esimerkiksi jotain tiettyä toista valintaa (esim. "paperi"), niin Markov-ketjuilla päästään tähän hyvin kiinni. Ketjun pituus on olla myös suurempi kuin yksi, jolloin huomioidaan useampi kuin yksi edellinen valinta. 

Markov-ketjua varten tarvitsen tietorakenteen, johon voin tallentaa pelaajan tekemiä valintoja ja tähän yhdistäen tiedot, mitä pelaaja on valinnan (tai valintojen) jälkeen pelannut. Koska ihminen ei todennäköisesti muista kovin pitkiä valintasarjoja, niin valitsen Markov-ketjun pituudeksi yksi, kaksi ja kolme. 

Tietorakenne määräytyy tavoitteena olevan algoritmin perusteella. Markov-ketjujen kanssa valintani on sanakirja, jossa avaimia ovat yksittäiset vaihtoehdot pelissä ja näiden kahden ja kolmen pituiset permutaatiot. Tällöin laajennetussa viiden vaihtoehdon pelissä sanakirjaan tulee yhteensä 5+25+125 avainta, eli yhteensä 155 avainta. Sanakirjassa jokaisen avaimen arvona on lista, johon tallennetaan kaikkien valintojen frekvenssit (avaimena olevan ketjun jälkeen). Näin tiedossa on valinta, joka on yleisin ja jota vastaan voidaan pelata. Toinen vaihtoehto olisi tähän huomioida nämä todennäköisyyksinä.


### Ongelma
Ongelma, jota pyrin ratkaisemaan, on vastustajan edellisten valintojen perusteella tehtävä valinta. Tavoitteena on siis löytää säännömukaisuuksia pelaajan pelistä ja sopeutua, jos käyttäytyminen muuttuu. Näitä valintoja varten minun pitää pitää muistissa pelaajan valinnat. Lista one helppokäyttöinen ja siiehn saa tallenettua järjestyksen. Jonon avulla voin lisätä ja poistaa myös alkiota näppärästi. Sanakirjan avulla on helppo toteuttaa haku ja tallennus, jossa on jokin määräävä asia (=avain).


### Syötteet
Syötteinä pelaaja antaa pelattavan vaihtoehdon, joka on tyyppiä str. Pelaajan valinnat ovat yksittäisiä merkkejä, jotka ovat jotka edustavat koko valintaa (esim. kivi -> k ).  


### Aika- ja tilavaativuudet
Koska syötteitä annetaan yksi kerrallaan ja kierrosten lukumäärä on melko pieni, niin aikavaativuus ei todennäköisesti ole kriittinen. Pyrin kuitenki välttämään aikavaativuutta O(n³) ja sitä suurempia aikavaativuuksia. Tilavaativuutta en ole vielä pohtinut. Itse asiassa tilavaativuus ei ole ollut tähän asti kovin paljon esillä käymilläni kursseilla. 


### Lähteet
[Laajennetun pelin säännöt](https://www.youtube.com/watch?v=x5Q6-wMx-K8) \
[Kurssimateriaalissa mainittu paperi Markov-ketjuen käytöstä](https://arxiv.org/pdf/2003.06769.pdf) \
[Wikipedian artikkeli Markov-ketjusta](https://en.wikipedia.org/wiki/Markov_chain)


### Muuta
Opinto-ohjelmani: Tietojenkäsittelytieteen kandidaatti (TKT). \
Dokumentaatiossa käytetty kieli on suomi. \
Projekti toteutetaan Pythonilla.
