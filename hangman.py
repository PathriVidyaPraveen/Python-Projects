# Here are some more exercises for you to try out on your own

# Update the code such that the count of 'guesses' updated only when you make a wrong guess. If you make a correct guess, then dont reduce the available count
# At the start of the game, don't mark all letters as blank - you can display a maximum of 2 consonants to help the user. The guessing game begins from this point - you can reduce total available guesses based on this update.


import time
import random

def choose_word():
    words = ['python', 'programming', 'treasure', 'creative', 'medium', 'horror']
    return random.choice(words)

def wordDisplay(word, guesses):
    display_word = ''
    for char in word:
        if char in guesses:
            display_word += char + ' '
        else:
            display_word += '_ '
    return display_word

def winningCondition(updated_word, turns):
    # Update your code below this line
     if '_' not in updated_word:
        result = 1
        return result
     if turns == 0:
        result = 0
        return result






if __name__ == '__main__':
    name = input("What is your name? ")
    print("Hello, " + name + ", time to play hangman!")
    time.sleep(1)
    print("Start guessing...\n")
    time.sleep(0.5)
    
    word = choose_word()
    turns = len(word)   # number of turns = length of the word to be guessed
    guesses = ''
    
    while turns > 0:
        print("\nYou have", turns, 'guesses remaining')
        print(wordDisplay(word, guesses))
        guess = input("\nguess a character: ").lower()
        
        if guess in guesses:
            print("\nYou have already tried this letter")
            continue
        else:
            guesses += guess
    
        if guess not in word:
            print("\nWrong, Try again")
        
        updated_word = wordDisplay(word, guesses)
        turns -= 1
        flag = winningCondition(updated_word, turns)
        
        if flag == 0:
            print("\nYou Lose")
            print("The word was", word)
        elif flag == 1:
            print("\nYou won!")
            print("You guessed", word, "correctly")
            break
    