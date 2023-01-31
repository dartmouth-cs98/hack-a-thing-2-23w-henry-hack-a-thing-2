from tokenize_from_file import *
from googletrans import Translator
from wordfreq import zipf_frequency
from google.cloud import translate

def get_candidates(filename, source_lang = "en", target_lang = "es"):
    candidates = frequency_dist(filename)

    quiz_candidates = []
    translator = Translator()

    for candidate in candidates.most_common(25):
        source_word = candidate[0].lower()
        translation = translator.translate(source_word, dest=target_lang, src=source_lang)

        target_word = translation.text.lower()

        if source_word != target_word and zipf_frequency(source_word, 'en') < 6:
            quiz_candidates.append((source_word, target_word, candidate[1]))
    
    return quiz_candidates

def get_quiz_words(filename, source_lang = "en", target_lang = "es", length=3):
    candidates = get_candidates(filename, source_lang, target_lang)

    quiz_words = candidates[:length]

    return quiz_words


