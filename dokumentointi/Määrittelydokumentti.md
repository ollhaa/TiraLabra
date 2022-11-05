# Määrittelydokumentti
---
### Ohjelmointikielet
Tämän työn ohjelmointikieli on Python. Olen Pythonia käyttänyt peruskursseilla sekä kursseilla TiRA 1 ja TiRa 2. 

Käytän jonkin verran työssäni R-kieltä, mutta ei taida olla tämän kurssin ja vertaisarvioitien kannalta olennaista. Lisäksi olen kokeillut hieman Javaa ja Haskelia, mutta varsinaista käyttötaitoa ei näillä kielillä ole.


### Valitut algoritmit ja tietorakenteet
Algoritmien käyttö on ns. kaksiosaista: Valinta pelissä perustuu eri pituisiin Markov-ketjuihin, mutta tämä pituutta optimoidaan edellisten valintojen perusteella säännöllisin(?) väliajoin. 

Tietorakenne määräytyy tavoitteena olevan algoritmin perusteella. Tällä hetkellä ajattelen, että tarvitsen listan, sanakirjan ja jonon. 


### Ongelma
Ongelma, jota pyrin ratkaisemaan, on vastustajan edellisten valintojen perusteella tehtävä valinta. Tavoitteena on siis löytää säännömukaisuuksia pelaajan pelistä ja sopeutua, jos käyttäytyminen muuttuu. Näitä valintoja varten minun pitää pitää muistissa pelaajan valinnat. Lista one helppokäyttöinen ja siiehn saa tallenettua järjestyksen. Jonon avulla voin lisätä ja poistaa myös alkiota näppärästi. Sanakirjan avulla on helppo toteuttaa haku ja tallennus, jossa on jokin määräävä asia (=avain).


### Syötteet
Tällä hetkellä syötteina on numerot 1,2,3, jotka edustavat kiveä, paperia ja saksia. Saatan muuttaa nämä kirjaimiksi. tältä osin aiheen syöte on yksinkertainen. 


### Aika- ja tilavaativuudet
Koska syötteitä annetaan yksi kerrallaan ja kierrosten lukumäärä on melko pieni, niin aikavaativuus ei todennäköisesti ole kriittinen. Pyrin kuitenki välttämään aikavaativuutta O(n³) ja sitä suurempia aikavaativuuksia. Tilavaativuutta en ole vielä pohtinut. Itse asiassa tilavaativuus ei ole ollut tähän asti kovin paljon esillä käymilläni kursseilla. 


### Lähteet
[Laajennetun pelin säännöt](https://www.youtube.com/watch?v=x5Q6-wMx-K8)
[Kurssimateriaalissa mainittu paperi Markov-ketjuen käytöstä](https://arxiv.org/pdf/2003.06769.pdf)


### Muuta
Opinto-ohjelmani: Tietojenkäsittelytieteen kandidaatti (TKT)
Dokumentaatiossa käytetty kieli on suomi.
