"""36-dars test dasturlari"""

import unittest
from python_36_lesson import eng_kattasi

#1
class Test_3son(unittest.TestCase):
    def test_3son(self):
        test = eng_kattasi()
        self.assertEqual(test,23)

unittest.main()










