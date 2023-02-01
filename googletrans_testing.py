import googletrans
from generate_quiz import *

filename = "sample_text/twins.txt"

# translator = Translator()
# print(translator.translate("hello", dest="es"))

print(get_candidates(filename))