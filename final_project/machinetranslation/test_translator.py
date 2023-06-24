import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        # Test for the translation of the word ‘Hello’.
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('hello'), 'hello')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        # Test for the translation of the word ‘Bonjour’.
        self.assertEqual(french_to_english('bonjour'), 'hello') 
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

unittest.main()