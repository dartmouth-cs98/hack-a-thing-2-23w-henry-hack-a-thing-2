from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from string import punctuation


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

def frequency_dist(filename):

    file_tokens = tokenize_from_file(filename)

    # remove stop words and tokens that are just punctuation
    stop_words = set(stopwords.words("english"))

    meaningful_tokens = []
    for token in file_tokens:
        if any(p in token for p in punctuation):
            continue
        if token not in stop_words:
            meaningful_tokens.append(token)

    frequency_dist = FreqDist(meaningful_tokens)

    return frequency_dist