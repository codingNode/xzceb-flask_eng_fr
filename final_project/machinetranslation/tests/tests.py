import unittest
from translator import french_to_english,english_to_french

class TestTextTranslator(unittest.TestCase):
    def test_enTofr(self):
        self.assertEqual(english_to_french('Hi'), 'Bonjour')
        self.assertEqual(english_to_french('travel'), 'voyager')
    
    def test_frToen(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Comment allez-vous'), 'How are you')

if __name__ == '__main__':
    unittest.main()
