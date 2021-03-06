import random
from words import words
import string

#! Some words from imported list aren't valid as include chars such as '-' and spaces.
#* Needs to keep selecting until a valid word is found.


def find_valid_word(words):
    word = random.choice(words)  #randomly chooses word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    print('Welcome to Hangman!')
    word = find_valid_word(words)
    #* keep track of what letters have already been guessed in the word
    word_letters = set(word)  #saves all of the letters of a word as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #keep track of what the user has guessed
    lives = 6
    print(hangman_figure(lives))

    #* Getting user input
    # Want to user to be able to keep guessing until they guess the word, while loop.
    #! While there are still letters in word_letters and lives left, keep interating through this code.
    while len(word_letters) > 0 and lives > 0:
        # Letters user has already guessed
        #! .join() method ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You currently have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
      
        # The current word is, inc - where the user hasn't guessed the letter yet
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter:').upper()
        #* If a valid letter in alphabet that hasn't beeen used yet
        #* add to used_letters set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            #* If letter just guessed is in the word, remove letter from word_letters
            if user_letter in word_letters:
                  word_letters.remove(user_letter)
            else:
                  lives = lives - 1 #removes life if incorrect guess
                  print(user_letter, 'is not in this word!')
                  print(hangman_figure(lives))
                  print(' ')
                 
        #* If user_letter that user entered is in used_letters, means the user has already used it before
        #! equals an invalid guess
        elif user_letter in used_letters:
                print(
                    'You have already used the letter', user_letter, ', please choose another!'
                )
            #! Case for invalid chars
        else:
                print('Invalid character. Please try again.')
  
  #gets here when len(word_letters == 0 or lives == 0)
    if lives == 0:
      print('GAME OVER! The word was', word) 
    else:
      print('Yay! You guessed the word', word, '!')
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = find_valid_word(words)
        hangman()

def hangman_figure(lives):
  stages = [    
                # Game over!
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # The head, torso, both arms, and 1 leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # The head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # The head, torso, and 1 arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # The head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # The head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
  ]
  return stages[lives]
  

if __name__ == '__main__':
    hangman()

