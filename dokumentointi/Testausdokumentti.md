# Testausdokumentti
---
### Yksikkötestaus
Yksikkötestit on suoritettu unittest-kirjaston avulla. Testit löytyvät tests-kansiosta. Testattavia luokkia ovat Markov ja Tekoaly. Käyttöliittymää ja pelilogiikkaa ei testata. 

Linux-ympäristössä testit voidaan suorittaa komennolla `poetry run invoke testcov`. Tämän jälkeen testikattavuudesta kertova raportti tallentuu kohteeseen `sovellus/htmlcov/index.html` 

![Kuva: Testikattavuus](https://github.com/ollhaa/TiraLabra/blob/main/dokumentointi/coverage.jpg)

### Luokkakohtaiset tiedot
**Markov** \
Testataan palauttaako luokan answer-metodi oikean valinnan. Tätä varten on valittu sopivasti historia, jotta päästään pois todennäköisyyksista.

**Tekoaly** \
Testataan pelattavan algoritmin asettamista ja saamista. Tätä tarvitaan varsinaisten algoritmien testaamiseen. Pelattavista algoritmeista testataan Markov-ketjuja pituuksilla 1-3. 

**Muuta** \
Ohjelman rakenteesta ja satunnaisuudesta johtuen testausta on tehty aputulosteiden avulla melko paljon. Esimerkiksi luokkia peliApp ja pelilogiikka on testattu tällä tavoin, kuten myös Tekoaly-luokan algoritmien vertailua. 
 
### Suorituskyky
Suorituskykyä on testattu "manuaalisesti" eri pelattavien vastustajien osalta kierrosten lukunmäärän ollessa 20, 100 tai 500 (vain Tekoaly). Testataan siis pelaa-funktion keskimääräistä aikaa. Teoriassa keskimääräisen ajan pitäisi kasvaa, kun valintoja tallennetaan enemmän ja luokkien keskimääräisen ajan pitäisi olla järjestyksessä satunnainen (=Sari Satunnainen) < Markov (= Marko Markov2) < Tekoaly (=Tekoaly). 

|    Luokka    |     n = 20     |     n = 100     |    n = 500    |
| ------------ | -------------- | --------------- | ------------- |
|    Random    | $6.97*10^{-5}$ | $6.80*10^{-5}$  | ei testattu   |
|    Markov    |  0.00010       |  0.00011        | ei testattu   |
|    Tekoaly   |  0.00013       |  0.00012        | 0.00025       |

Käytännössä näyttäisi siltä, että kierrosten lukumäärän kasvaessa keskimääräinen aika kasvaa, mutta tämä ei ole kriittistä pelin toiminnan kannalta. On hyvä huomata, että näissä on aina hieman satunnaisuutta mukana.

### Toiminta
Sovelluksen kannalta mielenkiintoista on tietysti se, miten hyvin se toimii käytännössä ja pystyy vastaamaan asetettuun tavoitteeseen: Voittaako tekoäly ihmispelaajan. Tämän kannalta välttämätöntä on, että tekoäly tunnistaa säännönmukaisuuksia ihmisen pelaamisessa ja toisaalta pystyy reagoimaan mahdollisiin pelitapamuutoksiin. Tältä osin testasin ainoastaan luokkaa Tekoaly, joka on sovelluksen tärkein osa.

**1. Pelataan järjestyksessä K-P-S-L-C:** \
Pelaajan pisteet: 15 ja tietokoneen 74. Yhteensä 100 kierrosta. Pelaajan voittoprosentti 16,85.

**2. Pelataan aina kaksi samaa valintaa peräkkäin (esim. KK-PP-CC-KK....)** \
Pelaajan pisteet: 33 ja tietokoneen 46. Yhteensä 100 kierrosta. Pelaajan voittoprosentti 41,77.

**3. Pelataan tiettyä valintaa yksi kerta, sitten toista kaksi kertaa ja sitten kolmatta valintaa 3 kertaa (esim. K-PP-CCC-P-KK-LLL...)** \
Pelaajan pisteet: 37 ja tietokoneen 40. Yhteensä 100 kierrosta. Pelaajan voittoprosentti 48,05.

**4. Pelataan ensin kymmenen kertaa KPPS, sitten kymmenen kertaa LC ja lopuksi taas kymmenen kertaa KPPS** \
Pelaajan pisteet: 16 ja tietokoneen 69. Yhteensä 100 kierrosta. Pelaajan voittoprosentti 18,82.

**5. Siskon poika, alle kymmenen vuotta** \
Pelaajan pisteet: 31 ja tietokoneen 47. Yhteensä 100 kierrosta. Pelaajan voittoprosentti 39,74. \
*Kommentti: Kierrosten edetessä samat valinnat toistuivat ja mielenkiinto taisi olla muualla. Eniten valintoja tutuista K/P/S.*

**6. Minä itse** \
Pelaajan pisteet: 39 ja tietokoneen 40. Yhteensä 100 kierrosta. Pelaajan voittoprosentti 49,37. \
*Kommentti: Yritin huomioida hieman taustalla olevaa tekoälyä muuttamalla pelityyliä pelin aikana. Lyhyemmissa peleissä pääsin kyllä voitolle.*

**7. Ensin seitsemän kertaa tiettyä valintaa, sitten K-P-S-L-C-K-P ja taas tiettyä valintaa seitsemän kertaa** \
Pelaajan pisteet: 33 ja tietokoneen 43. Yhteensä 100 kierrosta. Pelaajan voittoprosentti 43,42.

On kuitenkin hyvä huomata, että näitä jokaista pelattiin vain yksi kierros. Tekoäly kuitenkin tunnisti jotain tapoja hyvin tai melko hyvin.
