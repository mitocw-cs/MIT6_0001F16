# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str_letters_guessed = ''.join(letters_guessed)
    for word in secret_word:
        if str_letters_guessed.find(word) == -1:
            return False
    return True


# print("TEST is_word_guessed: ", is_word_guessed(secret_word='anhquan', letters_guessed=['e','a', 'n', 'b', 'h', 'l', 'q', 'u']))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str_letters_guessed = ''.join(letters_guessed)
    guessed_words = []
    for word in secret_word:
        if str_letters_guessed.find(word) != -1:
            guessed_words.append(word)
        else:
            guessed_words.append('_')
    return ''.join(guessed_words)


# print("TEST get_guessed_word: ", get_guessed_word(secret_word='apple', letters_guessed=['a', 'i', 's', 'l', 'r', 's']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = []
    tmp = ''.join(letters_guessed)
    for letter in alphabet:
        if tmp.find(letter) == -1:
            available_letters.append(letter)
    return ''.join(available_letters)

# print("TEST get_available_letters: ", get_available_letters(['a', 'c', 'y']))

def find_unique_characters(word):
    tmp, c = [], []
    for char in word:
        tmp.append(char)
    for i in range(0, 1234):
        c.append(0)
    for char in tmp:
        c[ord(char)] += 1
    counter = 0
    for i in range(0, 1234):
        if c[i]!= 0:
            counter += 1
    return counter

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_left = (len(secret_word) * 5) // 3
    print('Welcome to game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('---------------------------------')
    print('You have', guesses_left, 'guesses left.')
    print('Available letter: ', get_available_letters([]))
    print('---------------------------------')
    print("DEBUG, secrect_word = ", secret_word)
    letters_guessed = []
    warnings = 3
    while not is_word_guessed(secret_word, letters_guessed):
        input_letter = input('Please guess a letter: ')
        if guesses_left == 0:
            break
        else:
            guesses_left -= 1
        if warnings == 0:
            print('Whoops! You losed, warnings left! :(')
            print('secrect word: ', secret_word)
            return
        if not (str.lower(input_letter) and str.isalpha(input_letter)):
            warnings -= 1
            print('Oops! That is not valid letter. You have,', warnings, 'left: ', get_guessed_word(secret_word, letters_guessed))
        letters_guessed.append(input_letter)
        if input_letter in secret_word:
            print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops!, That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))

        print('You have', guesses_left, 'guesses left.')
        print('Available letter: ', get_available_letters(letters_guessed))
        print('---------------------------------')
    if is_word_guessed(secret_word, letters_guessed):
        print('Congrats you won! :)')
        print('secrect word: ', secret_word)
        u_chars_sw = find_unique_characters(secret_word)
        print('Your total score for this game: ', guesses_left*u_chars_sw)
    else:
        print('Whoops! You losed! :(')
        print('secrect word: ', secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = ''
    secret_word = choose_word(wordlist)
    hangman(secret_word)


    ###############

    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
