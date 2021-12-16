import unittest
import sys, os
from features.steps.builder import *

sys.path.append(os.getcwd())

class Clothes_Builder_Test(unittest.TestCase):
    director = Director()
    builder = Clothes_Builder()
    director.builder = builder
    def test_Bershka(self):
       print("Bershka: ")
       self.director.Bershka()
       self.builder.product.list_parts()

    def test_HM(self):
        print("\nHM: ")
        self.director.HM()
        self.builder.product.list_parts()

if __name__ == "__main__":
    unittest.main()