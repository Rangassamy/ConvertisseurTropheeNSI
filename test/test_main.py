# Exemple de test unitaire
import unittest

class TestConversion(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(2 * 2, 4)

if __name__ == '__main__':
    unittest.main()
