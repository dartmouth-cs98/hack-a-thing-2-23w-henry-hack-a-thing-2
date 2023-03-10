from tokenize_from_file import *
from googletrans import Translator
from wordfreq import zipf_frequency
from google_api import translate_text
from azure_api import azure_translate, azure_dictionary
import requests
from config import AZURE_KEY

from unidecode import unidecode # found here: https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string


def get_candidates(filename, length, source_lang = "en", target_lang = "es"):

    candidates_found = 0

    candidates = frequency_dist(filename)

    quiz_candidates = []

    for candidate in candidates.most_common(25):
        source_word = candidate[0].lower()

        # eliminate words that are too common (and therefore too easy)
        if not zipf_frequency(source_word, 'en') < 6:
            continue

        translation = azure_translate(source_word)

        target_word = unidecode(translation.lower())

        if source_word != target_word:
            quiz_candidates.append((source_word, target_word, candidate[1]))
            candidates_found += 1

            if candidates_found >= length:
                return quiz_candidates
    
    # currently possible to return fewer candidates than length, but not more
    return quiz_candidates

def get_quiz_words(filename, source_lang = "en", target_lang = "es", length=3):
    candidates = get_candidates(filename, length, source_lang, target_lang)

    quiz_words = candidates[:length]

    return quiz_words


def check_override(word, answer, source_lang = "en", target_lang = "es"):
    dictionary = azure_dictionary(word, source_lang, target_lang)[0]
    
    translations = dictionary['translations']

    for translation in translations:
        if translation['displayTarget'] == answer:
            return True
    
    return False




