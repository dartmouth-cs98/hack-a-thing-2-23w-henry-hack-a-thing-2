from tokenize_from_file import *
from googletrans import Translator

def get_candidates(filename, source_lang = "en", target_lang = "es"):
    candidates = frequency_dist(filename)

    quiz_candidates = []
    translator = Translator()

    for candidate in candidates.most_common(25):
        source_word = candidate[0].lower()
        translation = translator.translate(source_word, dest=target_lang, src=source_lang)

        target_word = translation.text.lower()

        if source_word != target_word:
            quiz_candidates.append((source_word, target_word))
    
    return quiz_candidates
