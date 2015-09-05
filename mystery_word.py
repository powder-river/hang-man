import random

# opens the apple dictonary and saves the words from the apple dictonary
# into a list
with open('/usr/share/dict/words') as w:
    word_dictionary = w.read()
    word_dictionary = word_dictionary.split()


#Returns a filtered version of the word list with words only containing
#4-6 characters.
def easy_words(word_list):
    filterd_list = []
    for word in word_list:
        if len(word) >=4 and len(word) <= 6:
            filterd_list.append(word)
    return filterd_list


# Returns a filtered version of the word list with words only containing
# 6-8 characters.
def medium_words(word_list):
    filterd_list = []
    for word in word_list:
        if len(word) >=6and len(word) <= 8:
            filterd_list.append(word)
    return filterd_list


# Returns a filtered version of the word list with words only containing
# 8+ characters.
def hard_words(word_list):
    filterd_list = []
    for word in word_list:
        if len(word) >7:
            filterd_list.append(word)
    return filterd_list


# Returns a random word from the word list.
def random_word(word_list):
    pick_a_word = random.randint(0,len(word_list))
    return word_list[pick_a_word]


#takes the word and converts it to underscores
def display_word(word, guesses):
    underscore_word = []
    answer = []
    incorrect_guesses = []

    #iterates over each letter and puts it into a list
    #then it iterates over that list and turns each letter into an _
    for n in word:
        answer.append(n)
    for n in range(len(answer)):
        if answer[n].isalpha():
            underscore_word.append("_")

    #takes the guess (which is in the form of a list),
    #upcases it, if true displays the letter in the word
    #takes the word from a list and turns it into a string with each letter
    #seperated by a space
    for g in guesses:
        for n in range(len(answer)):
            if g == answer[n]:
                underscore_word[n] = g.upper()
    return " ".join(underscore_word)


#Returns True if the list of guesses covers every letter in the word,
#otherwise returns False.
def is_word_complete(word, guesses):
    underscore_list = display_word(word,guesses).split()
    underscore_list = "".join(underscore_list)

    if underscore_list == word.upper():
        return True
    else:
        return False


#puts all the functions together and runs the program
def main():
    #variables
    difficulty = input("Enter a Difficuty Level, e for easy, m for medium, or h for hard...\n")
    attempts  =  13
    guessed_words = []

    #starts the game, prompts the user for difficulty level
    #chooses a word based off of the difficulty
    if difficulty.lower() == 'e':
        game_word = easy_words(word_dictionary)
    elif difficulty.lower() == 'm':
        game_word = medium_words(word_dictionary)
    elif difficulty.lower() == 'h':
        game_word = hard_words(word_dictionary)
    else:
        print("invalid inupt")

    #this is where the game is played. shows a blank slate and fills in
    #the correct letters as they are guessed
    game_word = random_word(game_word)
    while attempts > 0 and is_word_complete(game_word,guessed_words) == False:
        user_guess = input("Guess a letter\n")
        guessed_words.append(user_guess)
        print(display_word(game_word, guessed_words))
        attempts -= 1
        print("You have guessed", guessed_words)
        print("You have {} guesses remaining".format(attempts))


    #tells the user if they have won or not, and ask if they want to play again
    if is_word_complete(game_word,guessed_words) == False:
        print("You have lost, the answer was",game_word)
        again = input("Play Again? y/n")
        if again.lower() == "y":
            main()
    else:
        print("CORRECT!!!! The answer was",game_word)
        again = input("Play Again? y/n")
        if again.lower() == "y":
            main()


if __name__ == '__main__':
    main()
