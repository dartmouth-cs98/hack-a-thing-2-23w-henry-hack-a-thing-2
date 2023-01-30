from generate_quiz import get_quiz_words

filename = "sample_text/twins.txt"

quiz_words = get_quiz_words(filename)

print("welcome to your quiz")

score = 0

for word in quiz_words:
    print("translate {}".format(word[0]))
    answer = input("Your answer: ")

    if answer == word[1]:
        print("Correct!")
        score += 1
    else:
        print("Sorry, incorrect. Correct answer is \'{}\'".format(word[1]))


print("You scored {}/{}".format(score, len(quiz_words)))