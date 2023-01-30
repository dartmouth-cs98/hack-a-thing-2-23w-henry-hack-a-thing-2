from nltk import word_tokenize
from nltk.corpus import stopwords


def tokenize_from_file(filename):
    file = open(filename, "r")

    file_text = file.read()

    tokens = word_tokenize(file_text)

    return tokens


def frequency_count(filename):
    tokens = tokenize_from_file(filename)

    stop_words = set(stopwords.words("english"))

    frequency_table = {}

    for token in tokens:
        if token in stop_words:
            continue

        if token not in frequency_table:
            frequency_table[token] = 1
        else:
            frequency_table[token] += 1

    return frequency_table