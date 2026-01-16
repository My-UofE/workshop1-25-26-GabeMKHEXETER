import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    #comapare current value and the next
    #check if user input is correct logically
    #return boolean 
    if (current_val > next_val and user_input == "l") or (current_val < next_val and user_input == "h"):
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    #letter = user input
    #word = selected word from .txt file
    #board = missing letters
    #check if the letter exists in the word at ALL 
    #replace blank spaces in board with letter if it exists
    #return boolean
