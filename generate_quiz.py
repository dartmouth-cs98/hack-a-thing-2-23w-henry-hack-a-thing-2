from tokenize_from_file import *
from googletrans import Translator
from wordfreq import zipf_frequency
from google_api import translate_text

def get_candidates(filename, source_lang = "en", target_lang = "es"):
    candidates = frequency_dist(filename)

    quiz_candidates = []

    for candidate in candidates.most_common(25):
        source_word = candidate[0].lower()
        translation = translate_text(source_word)[0].translated_text

        target_word = translation.lower()

        if source_word != target_word and zipf_frequency(source_word, 'en') < 6:
            quiz_candidates.append((source_word, target_word, candidate[1]))
    
    return quiz_candidates

def get_quiz_words(filename, source_lang = "en", target_lang = "es", length=3):
    candidates = get_candidates(filename, source_lang, target_lang)

    quiz_words = candidates[:length]

    return quiz_words


