from generate_quiz import get_quiz_words, check_override

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
        o = input("Think you're right? Press o to check synonyms, press anything else to continue: ")

        if o == "o":
            if check_override(word[0], answer):
                print("Correct!")
                score += 1
            else:
                print("Sorry, still no.")


print("You scored {}/{}".format(score, len(quiz_words)))