from tokenize_from_file import *

filename = "sample_text/twins.txt"

freq_dist = frequency_dist(filename)

print(freq_dist.most_common(20))



