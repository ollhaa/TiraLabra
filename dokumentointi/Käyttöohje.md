### Käyttöohje
---
Tämä sisältää asennus- ja käyttöohjeet sovellukselle.

## Vaatimukset
  * python 3.8 tai uudempi 
  * poetry 1.2.2 tai uudempi

## Asennus
Kloonaa repositio koneelle ja suorita `poetry install` hakemistossa sovellus.

## Käynnistäminen Linuxilla
Suorita komento `poetry run invoke start` hakemistossa sovellus.

## Käyttöliittymä
Ensin valitaan vastustaja komennoilla 1, 2 tai 3.
  * `1` = Sari - Sari Satunnainen. Tällöin tietokone pelaa puhasta satunnaisvalintaa.
  * `2` = Marko Markov2. Tietokone pelaa alun jälkeen toisen asteen Markov-ketjuihin perustuvaa valintaa. 
  * `3` = Tekoäly. Nyt tietokone pelaa varsinaista tekoälyä alun satunnaisvalinnan jälkeen.

Tämän jälkeen valitaan pelattava siirto: 
  * `k` = Kivi
  * `p` = Paperi
  * `s` = Sakset
  * `l` = Lisko 
  * `s` = Spock
  
Jokaiselle valinnalle on kaksi voittavaa siirtoa ja vastaavasti jokainen valinta voittaa kaksi muuta siirtoa. Esim. Kivi voittaa Sakset ja \
Liskon, mutta häviää Paperille ja Spockille.

![Siirrot](https://github.com/ollhaa/TiraLabra/blob/main/dokumentointi/Rock_paper_scissors_lizard_spock_rules.png)

[Pelin esittely tarkemmin](https://www.youtube.com/watch?v=x5Q6-wMx-K8)

  * Komennolla `q` peli päättyy ja ohjelma tulostaa yhteenvedon pelistä.
  
## Testaus
  * Suorita komento `poetry run invoke testcov` hakemistossa `sovellus`
  * Testikattavuudesta kertova raportti tallentuu kohteeseen `sovellus/htmlcov/index.py`

## Lint
  * Suorita komento `poetry run invoke lint` hakemistossa `sovellus`


