from nltk import word_tokenize


def tokenize_from_file(filename):
    file = open(filename, "r")

    file_text = file.read()

    tokens = word_tokenize(file_text)

    return tokens