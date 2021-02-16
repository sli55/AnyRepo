# Jumble.py
# Song Li
# Email: sli55@kent.edu

# import the English word set
from english_words import english_words_set as words

import collections

import random

# functions of solving a Jumble word puzzle
def sort(jumbled):
    
    find = []

    letters_jumbled = list(jumbled)

    for word in words:
        if len(word) == len(jumbled):
            letters_word = list(word)
            if collections.Counter(letters_word) == collections.Counter(letters_jumbled):
                find.append(word)
    return find

def solve():
    while True:
        jumbled_word = input("Enter the jumbled word that needs to be solved: ")

        solutions = sort(jumbled_word)

        # for different outcomes
        if len(solutions) == 0:
            print("")
            print("No matching items. ")
        if len(solutions) == 1:
            print("")
            print("Possible solution is:", ", ".join(solutions))
        if len(solutions) > 1:
            print("")
            print("Possible solutions are:", ", ".join(solutions))

        option = input("Press Enter to continue. Press 1 to exit: ")
        if option == "1":
            break
        else:
            print("--------------------------------------------------------------")
    return

# functions of playing a Jumble word game
def get_word():
    # random.choice() function returns a random element from the list given
    get = random.choice(sorted(words))
    return get

def jumble(word):
    # random.sample() function shuffles the word into letters
    shuffled = random.sample(word, len(word))

    # the "".join() function joins the letters into a word
    jumbled = "".join(shuffled)
    return jumbled

def game():
    while True:
        # get a random word
        random_word = get_word()

        # jumble the random word
        jumbled_word = jumble(random_word)

        # show answer for testing
        print("Answer for testing:    ", random_word)
        
        print("Here is a jumbled word:", jumbled_word)

        answer = input("Your answer is:         ")

        solutions = sort(jumbled_word)
        
        if answer in  solutions:
            print("")
            print("Your answer is Correct. ")

            opt1 = input("Press Enter to continue. Press 1 to exit: ")
            if opt1 == "1":
                break
            else:
                print("--------------------------------------------------------------")
        else:
            print("")
            print("Your answer is Wrong. The correct answer is:", random_word)

            opt2 = input("Press Enter to continue. Press 1 to exit: ")
            if opt2 == "1":
                break
            else:
                print("--------------------------------------------------------------")
    return

# main function
print("--------------------------------------------------------------Start")
print("Enter 1 to solve a Jumble puzzle. ")
print("Enter 2 to play a Jumble game. ")

option = input('Your option: ')
if option == "1":
    print("--------------------------------------------------------------Solving")
    solve()
if option == "2":
    print("--------------------------------------------------------------Playing")
    game()
print("--------------------------------------------------------------End")
