import unittest
from markov import Markov

class TestMarkov(unittest.TestCase):
    '''
    Luokka, jonka avulla testataan luokkaa Markov
    '''
    def setUp(self):
        '''
        Alustaa testausta
        '''
        self.markov = Markov()

    def test_markov2(self):
        '''
        Testaa luokan funktiota
        '''
        historia = {"KK":[3,0,0,0,0], "PP":[0,4,0,0,0], "CL":[0,0,3,0,0], "SC":[0,0,0,5,0], "LK":[0,0,0,0,3]}
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "K", "K"], kierrokset = 2, valinta = "K"), ("P", "C"))
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "P", "P"], kierrokset = 2, valinta = "K"), ("S", "L"))
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "C", "L"], kierrokset = 2, valinta = "K"), ("K", "C"))
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "S", "C"], kierrokset = 2, valinta = "K"), ("K", "S"))
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "L", "K"], kierrokset = 2, valinta = "K"), ("P", "L"))

if __name__ == "__main__":
    unittest.main()
