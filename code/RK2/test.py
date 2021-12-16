import unittest
import sys, os

sys.path.append(os.getcwd())
from RK2 import *

class TddTest(unittest.TestCase):
    def test_first_task(self):
        one_to_many = [(p.nameProg, p.memory, c.name)
                       for c in comps
                       for p in progs
                       if p.comp_id == c.id]
        self.assertEqual(first_task(one_to_many), [('Adobe Premiere Pro', 'Asus')])

    def test_2(self):
        one_to_many = [(p.nameProg, p.memory, c.name)
                       for c in comps
                       for p in progs
                       if p.comp_id == c.id]
        self.assertEqual(second_task(one_to_many),[('Acer', 200), ('Xiaomi', 450), ('HP', 580), ('Asus', 1150)])

    def test_3(self):
        many_to_many_temp = [(c.name, pc.comp_id, pc.prog_id)
                             for c in comps
                             for pc in progs_comps
                             if c.id == pc.comp_id]

        many_to_many = [(p.nameProg, p.memory, comp_name)
                        for comp_name, comp_id, prog_id in many_to_many_temp
                        for p in progs if p.id == prog_id]
        self.assertEqual(third_task(many_to_many),
                         [('Adobe Premiere Pro', 'Asus'), ('Adobe Premiere Pro', 'Apple'), ('Discord', 'Acer'),
                          ('Discord', 'Apple'), ('Figma', 'Xiaomi'), ('Figma', 'Lenovo'), ('PyCharm Community', 'HP'),
                          ('PyCharm Community', 'Lenovo'), ('Sony Vegas Pro', 'Acer'), ('Sony Vegas Pro', 'Apple')]
                         )

if __name__=='__main__':
    unittest.main()