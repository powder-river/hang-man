import random
print(random.randint(0,2))
word_list_ex = ["red", "blue", "green", "interesting"]
def easy_words(word_list):
    #Returns a filtered version of the word list with words only containing
    #4-6 characters.
    filterd_list = []
    for word in word_list:
        if len(word) >=4 and len(word) <= 6:
            filterd_list.append(word)
    return filterd_list


def medium_words(word_list):
    # Returns a filtered version of the word list with words only containing
    # 6-8 characters.

    filterd_list = []
    for word in word_list:
        if len(word) >=6and len(word) <= 8:
            filterd_list.append(word)
    return filterd_list


def hard_words(word_list):
    # Returns a filtered version of the word list with words only containing
    # 8+ characters.
    filterd_list = []
    for word in word_list:
        if len(word) >7:
            filterd_list.append(word)
    return filterd_list


def random_word(word_list):
    # Returns a random word from the word list.
    pick_a_word = random.randint(0,len(word_list))
    return word_list[pick_a_word]


def display_word(word, guesses):
    #takes the word and converts it to underscores
    underscore_word = []
    answer = []
    incorrect_guesses = []
    for n in word:
        answer.append(n)
    for n in range(len(answer)):
        if answer[n].isalpha():
            underscore_word.append("_")

    #takes the guess (which is in the form of a list),
    #upcases it, if true displays the letter in the word
    for g in guesses:
        for n in range(len(answer)):
            if g == answer[n]:
                underscore_word[n] = g.upper()
    return " ".join(underscore_word)


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    underscore_list = display_word(word,guesses).split()
    underscore_list = "".join(underscore_list)

    if underscore_list == word.upper():
        return True
    else:
        return False

    de_bug = []
    # underscore_list = display_word(word,guesses).split()
    # for n in range(len(underscore_list)):
    #     if underscore_list[n] == "_":
    #         de_bug.append("x")
    #     else:
    #         de_bug.append("o")

    return underscore_list

print(is_word_complete("beue",["e","b","u"]))
def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    # TODO


if __name__ == '__main__':
    main()
