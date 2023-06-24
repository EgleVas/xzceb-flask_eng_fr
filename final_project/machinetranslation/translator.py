"""Module for en-fr and fr-en translations"""
import json
import os

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """This function returns English text translated to French"""
    #write the code here
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """This function returns French text translated to English"""
    #write the code here
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text
