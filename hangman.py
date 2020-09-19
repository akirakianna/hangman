import random
from words import words
import string

#! Some words from imported list aren't valid as include chars such as '-' and spaces.
#* Needs to keep selecting until a valid word is found.

def find_valid_word(words):
  word = random.choice(words) #randomly chooses word from list
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()

def hangman():
  word = find_valid_word(words)
  #* keep track of what letters have already been guessed in the word
  word_letters = set(word) #saves all of the letters of a word as a set
  alphabet = set(string.ascii_uppercase)
  used_letters = set() #keep track of what the user has guessed

#* Getting user input
  user_letter = input('Guess a letter:').upper()
  #* If a valid letter in alphabet that hasn't beeen used yet
  #* add to used_letters set
  if user_letter in alphabet - used_letters:
    used_letters.add(use)
   #* If letter just guessed is in the word, remove letter from word_letters
    if user_letter in word_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
   #* If user_letter that user entered is in used_letters, means the user has already used it before
   #! equals an invalid guess
    elif user_letter in used_letters:
      print('You have already used this letter! Please choose another.')
    #! Case for invalid chars
    else: 
      print('Invalid character. Please try again.')

user_input = input('Type something:')
print(user_input)

