import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("hello"), "bonjour") # Test for the translation of the word ‘Hello’ and ‘Bonjour’.
        #self.assertEqual(englishToFrench('Hello'), 'FR')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("bonjour"), "hello") # Test for the translation of the word ‘Bonjour’ and ‘Hello’.
        #self.assertEqual(frenchToEnglish('Hello'), 'EN')

unittest.main()