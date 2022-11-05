# Viikko 1
---
### Mitä olen tehnyt tällä viikolla?
Aloitin tutustumalla mahdollisiin aiheisiin. Pohdin eri aiheiden vaikeusastetta ja mielenkiintoa. Olen aina ollut kiinnostunut erilasista peleistä, joten ns. laajennettu(?) KPS vaikutti erityisen hauskalta vaihtoehdolta. Keskusteltuani ohjaajan kanssa sain uskoa siihen, että pystyn tämän toteuttamaan.

Kokeilin hieman koodailla ja totetutin yksinkertaisen tekstikäyttöliittymän ja kaksi mahdollista vastustajaa: Satunnaisen valinnan sekä 2-asteisen Markov-ketjun. Nämä onnistuivat melko helposti. 

Lisäksi etsin tietoa ja selvitin kurssiin liittyviä käytäntöjä. 


### Miten ohjelma on edistynyt?
Ohjelma on edistynyt kohtuullisesti. Toteutin kivi-paperi-sakset -pelin (vasta näillä kolmella vaihtoehdolla) ja tein siihen vastustajaksi satunnaisvalinnan ja 2-asteiden Markov-ketjun. Nämä näyttäisivät toimivan hyvin ja ohjelmaa voi pelata tekstikäyttöliittymän kautta. 


### Mitä opin viikolla?
Opin viikolla tämän laajennetun KPS:n säännöt ja Markov-ketjujen käytöstä pelissä. Tämä ns. aiempiin valintoihin perustuva "tekoäly" vaikuttaa samaan aikaan yksinkertaiselta ja toimivalta. Lisäksi törmäsin erilaisiin muihin vaihtoehtoihin, joilla tietokoneen valintoja voidaan toteuttaa. Osa näistä vaikuttaa melko monimutkaisilta.


### Mikä jäi epäselväksi tai on tuottanut vaikeuksia?
Tällä hetkellä epäselvää on se, millaisen tietorakenteen valitsen "muistamaan" pelaajan valinnat. Todennäköisesti tarvitsen sekä listan että jonkin toisen tietorakenteen (jono, sanakirja, muu). Tämä valinta liittyy olennaisesti myös pelin aikavaativuuteen. Koska pelaajan syötteet ovat yksittäisiä kirjaimia tai numeroita ja kierrosten lukumäärä on verrattain pieni (<1000), niin tämä ei välttämättä ole kriittinen asia. Pelin on kuitenkin toimittava sujuvasti ilman odottelua. 

Epäselvää on myös tulevan testauksen ja mahdollisen graaffisen käyttöliittymän toteuttaminen. Nämä eivät ole vielä huolenaiheitani. 


### Mitä teen seuraavaksi?
Seuraavaksi aloitan toteuttamaan algoritmia, joka valitsee esim. viiden kierroksen jälkeen uuden algoritmin, joka puolestaan valitsee tietokoneen vastauksen. Käytännössä taustalla siis pelataan esim. 1-5 asteen Markov-ketjua ja tietyin väliajoin valitaan se, joka olisi voittanut eniten edellisillä kierroksille. Teen tämän ensin perinteiselle KPS:lle ja sitten mahdollisesti laajennan tätä siihen viiden vaihtoehdon peliin.


### Tuntikirjanpito


2.11.2022: 2 tuntia: Omatoimista tutustumista aiheisiin ja hieman koodailua.
3.11.2022: 2 tuntia: Keskustelua ohjaajan kanssa ja hieman koodailua.
4.11.2022: 1 tunti: Lisää lukemista ja tietorakenteiden pohtimista.
5.11.2022: 3 tuntia: Viikkoraportin tekemistä ja dokumentaatiota. 
