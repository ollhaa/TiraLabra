import unittest

from Markov import Markov

class TestMarkov(unittest.TestCase):
    
    def test_found(self):
        historia = {'R': [1, 1, 0], 'P': [1, 0, 1], 'S': [0, 1, 1], 'RR': [0, 0, 0], 'RP': [0, 0, 1], 'RS': [0, 0, 0], 'PR': [1, 2, 0], 'PP': [0, 0, 0], 'PS': [0, 0, 1], 'SR': [0, 0, 0], 'SP': [1, 0, 0], 'SS': [0, 1, 0], 'RRR': [0, 0, 0], 'RRP': [0, 0, 0], 'RRS': [0, 0, 0], 'RPR': [0, 0, 0], 'RPP': [0, 0, 0], 'RPS': [0, 0, 1], 'RSR': [0, 0, 0], 'RSP': [0, 0, 0], 'RSS': [0, 0, 0], 'PRR': [0, 0, 0], 'PRP': [0, 0, 0], 'PRS': [0, 0, 0], 'PPR': [0, 0, 0], 'PPP': [0, 0, 
        0], 'PPS': [0, 0, 0], 'PSR': [0, 0, 0], 'PSP': [0, 0, 0], 'PSS': [0, 1, 0], 'SRR': [0, 0, 0], 'SRP': [0, 0, 0], 'SRS': [0, 0, 0], 'SPR': [1, 0, 0], 'SPP': [0, 0, 0], 'SPS': [0, 0, 0], 'SSR': [0, 0, 0], 'SSP': [1, 0, 0], 'SSS': [0, 0, 0]}
        #edelliset = ["P","R", "P", "S"]
        #nimi = "Mark Markov2"
        #kierrokset = 2
        m = Markov()

        self.assertEqual(m.Answer(historia = historia,edelliset =["R", "P", "S"], nimi="Mark Markov2",kierrokset = 2,valinta="R"), "R")
        self.assertEqual(m.Answer(historia = historia,edelliset =["R", "P", "S"], nimi="Mark Markov2",kierrokset = 6,valinta="S"), "R")
        self.assertEqual(m.Answer(historia = historia, edelliset =["R", "R", "P"], nimi="Mark Markov2",kierrokset = 2,valinta="R"), "R")


if __name__ == "__main__":
    unittest.main()
