import unittest
from tekoaly import Tekoaly

class TestTekoaly(unittest.TestCase):
    '''
    Luokka, jonka avulla testataan luokkaa Tekoaly
    '''
    def setUp(self):
        '''
        Alustaa testausta
        '''
        self.markov = Tekoaly()

    def test_setter(self):
        '''
        Testaa Tekoaly-luokan pelattavan algoritmin asettajaa.
        '''
        self.markov.set_pelattava(1)
        self.assertEqual(self.markov.get_pelattava(),1)
        self.markov.set_pelattava(3)
        self.assertEqual(self.markov.get_pelattava(),3)
        self.markov.set_pelattava(5)
        self.assertEqual(self.markov.get_pelattava(),5)

    def test_tekoaly1(self):
        '''
        Testaa Tekoaly-luokan algoritmia 1
        '''
        self.markov.set_pelattava(1)
        historia = {"K":[3,0,0,0,0],"C":[0,4,0,0,0], "KK": [0,0,0,0,1], "PP":[0,0,2,0,0],
        "KC":[1,0,0,0,0], "CL":[0,0,0,4,0], "KPC": [0,0,0,0,3],
        "KKC": [0,0,0,4,0], "KKK": [3,0,0,0,0]}
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "K", "K"], kierrokset = 2, valinta = "K"), ("P", "C"))
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "K", "C"], kierrokset = 2, valinta = "K"), ("S", "L"))

    def test_tekoaly2(self):
        '''
        Testaa Tekoaly-luokan algoritmia 2
        '''
        self.markov.set_pelattava(2)
        historia = {"K":[3,0,0,0,0],"C":[0,4,0,0,0], "KK": [0,0,0,0,1], "PP":[0,0,2,0,0],
        "KC":[1,0,0,0,0], "CL":[0,0,0,4,0], "KPC": [0,0,0,0,3],
        "KKC": [0,0,0,4,0], "KKK": [3,0,0,0,0]}
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "K", "K"], kierrokset = 2, valinta = "K"), ("P", "L"))
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "K", "C"], kierrokset = 2, valinta = "K"), ("P", "C"))

    def test_tekoaly3(self):
        '''
        Testaa Tekoaly-luokan algoritmia 3
        '''
        self.markov.set_pelattava(3)
        historia = {"K":[3,0,0,0,0],"C":[0,4,0,0,0], "KK": [0,0,0,0,1], "PP":[0,0,2,0,0],
        "KC":[1,0,0,0,0], "CL":[0,0,0,4,0], "KPC": [0,0,0,0,3],
        "KKC": [0,0,0,4,0], "KKK": [3,0,0,0,0]}
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "K", "K"], kierrokset = 2, valinta = "K"), ("P", "C"))
        self.assertIn(self.markov.answer(historia=historia, edelliset = ["P","S", "C", "L", "K", "K", "C"], kierrokset = 2, valinta = "K"), ("K", "S"))

if __name__ == "__main__":
    unittest.main()
