import unittest
from kvadrat import yuza,perimetr

class Test_kvadrat(unittest.TestCase):
    """Kvadrat bilan bog'liq ammallarni test qiluvchi klass"""
    def test_yuza(self):
        """Kvadrat yuzini test qiluvchi funksia"""
        self.assertAlmostEqual(yuza(4),16)
        self.assertAlmostEqual(yuza(6),36)
        
    def test_peimetr(self):
        """Kvadrat yuzini test qiluvchi funksia"""
        self.assertAlmostEqual(perimetr(3),12)
        self.assertAlmostEqual(perimetr(8),32)

unittest.main()
