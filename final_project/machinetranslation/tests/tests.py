import unittest
from translator import englishToFrench, frenchToEnglish

class test_EnglishFrench(unittest.TestCase):
    def test_english(self):
        self.assertEqual(englishToFrench('Dog'), 'Chien')
        self.assertEqual(englishToFrench('Sun'), 'Soleil')
        self.assertNotEqual(englishToFrench('None'), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_french(self):
        self.assertEqual(frenchToEnglish('Robe'), 'Dress')
        self.assertEqual(frenchToEnglish('Soleil'), 'Sun')
        self.assertNotEqual(frenchToEnglish('None'), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()