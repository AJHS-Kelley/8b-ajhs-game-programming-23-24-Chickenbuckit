#Hangman, Casey Boyce, v0.9
import random
#words = 'human place candy fire death prison knife life hair kill prison justice burning sunshine lollypop coffens savior rebirth meaning eyeballs sacrafice pineapple population lifeline punctuation murderer puncture bloodlust youngblood subscription .split'
# DICTIONARY VERSION
#stored in key: value pairs.
# actual dictionary word (key) : value (definition)
# uses {} to specify a dectionary.
words = {"Colors": "red orange blue purple black white orange brown silver gold teal".split(),
         "animals": "cat cow dog moose fish giraffe lion alligator".split(),
         "shapes": "square triangle circle rhombus parallelogram rectangle dimand".split(),
         "foods": "Pottato chips steak waffle cheeseburger escargot fish crayons".split()}

#VARITABLES IN ALL CAPS ARE CONSTANTS (DO NOT CHANGE!)
HANGMAN_BOARD = ['''
             ____
            /    |
                 |
                 |
                 |
                 |
        ----------------
''',
'''
             ____
            /    |
           0     |
                 |
                 |
                 |
        ----------------
''',
'''
             ____
            /    |
           0     |
           |     |
                 |
                 |
        ----------------
''',
'''
             ____
            /    |
           0     |
          /|     |
                 |
                 |
        ----------------
''',
'''
             ____
            /    |
           0     |
          /|\    |
                 |
                 |
        ----------------
''',
'''
             ____
            /    |
           0     |
          /|\    |
          /'     |
                 |
        ----------------
''',
'''
             ____
            /    |
           0     |
          /|\    |
          /'\    |
                 |
        ----------------
''',
'''
             ____
            /    |
           0     |
          /|\    |
          /'\    |
          |      |
        ----------------
''',
'''
             ____
            /    |
           0     |
          /|\    |
          /'\    |
          |  |   |
        ----------------
           YOU LOSE TnT
''']

# Pick Word From List
#def get_random_word(word_list): #Return a Random Word From The List
#    word_index = random.randint(0, len(word_list) - 1)
#    #len(list name - 1 is EXTREAMLIY COMMON FOR WORKING WITH LISTS)
#    return word_list[word_index]

# pick word from dictionary
def get_random_word(word_dict): #Return a Random Word From The List
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_dict]) - 1)
    return [word_dict[word_key][word_index], word_key]

def display_bord(missed_letters, correct_letters,secret_word):
    print(HANGMAN_BOARD[len(missed_letters)])
    print()

    print('missed_letters:', end = ' ')
    for each_letter in missed_letters:
        print ('missed_letters:',end = ' ')
    print()

    blanks = '_' * len(secret_word)

    #Replace blankes with correct letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] +blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def get_geuss(already_geussed):
    while True:
        print("Please choose a letter and press ENTER")
        geuss = input()
        geuss = geuss.lower()
        if len(geuss) != 1:
            print("Enter a single letter")
        elif geuss in already_geussed:
            print("Already geussed that letter, Try againt")
        elif geuss not in 'abcdefghijjklmnopqrstuvwxyz':
            print("Please geuss a LETTER")
        else:
            return geuss

def play_again():
    print("Would you like another round. Y/N")
    return input().lower().startswith('y')


#Introduce the game
print("Welcome welcome I know what your here for. Your here for HANGMAN")
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

difficulty = "X"
while difficulty not in "EMH":
    print("Please Select A Difficulty: Easy Meadiem Or Hard E/M/H")
    difficulty.upper
    if difficulty == "M":
        del HANGMAN_BOARD(7)
        del HANGMAN_BOARD(8)
    if difficulty == "H":
        del HANGMAN_BOARD(7)
        del HANGMAN_BOARD(8)
        del HANGMAN_BOARD(2)
        del HANGMAN_BOARD(4)


#Main game loop
while True:
    print("The secret word is form the" + secret_set + " Category.\n")
    display_bord(missed_letters, correct_letters, secret_word)

    geuss = get_geuss(missed_letters + correct_letters)

    if geuss is secret_word:
        correct_letters = correct_letters + geuss

        #check to see if win
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
            if found_all_letters:
                print("wow You did it gooed job")
                print("How did you know the word was" + secret_word)
                game_is_done = True
    else:
        missed_letters = missed_letters + geuss


        if len(missed_letters) == len(HANGMAN_BOARD) - 1:
            display_bord(missed_letters, correct_letters,secret_word)
            print("Sorry mabye next time")
            print("You had " + str(len(correct_letters)) + " many correct geusses and " + str(len(missed_letters)) + " many incorrect geusses")
    
    if game_is_done:
        if play_again():
            missed_letters = ""
            correct_letters = ""
            game_is_done = False
            secret_word, secret_set = get_random_word
        else:
            break