# Problem Set 4, hangman.py
# Collaborators: Nada Chehab
# Time spent: Struggled until Tuesday with the assignment so decided to reach out Wednesday.
# Approx 5 hours over the phone at which point I decided to trash my code since I was getting more confused writing my own and 
# following hers. 
# Throughout the day on Wednesday. Touched based on Thursday. Had my conference presentation Friday.
# Saturday worked out a plan for me to finish and review with her on Sunday. She's been avail able to me throughout the weekend when I get stuck.
# So IDK how many real hours but a lot.
#
# 11/1/2020 another review with Nada
# 11/5, 11/6, 11/10, 11/13 worked with tutor
# 
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

#%%
import random
import string
import os.path
WORDLIST_FILENAME = "words.txt"


def load_words(silent=False):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    if(not silent):
      print("Loading word list from file...")
    global WORDLIST_FILENAME
    # inFile: filek
    if os.path.exists("psets/4/words.txt"):
      WORDLIST_FILENAME = "psets/4/"+WORDLIST_FILENAME
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
#%%
# Create a function 1A) Determine whether the word has been guessed
# boolean returned either the word is guessed or not 
# two parameters into this function to see if the secret_word is equal to the word quessed
# using letters guessed at i are not in secret_word - every letter is compared to the word

def is_word_guessed(secret_word, letters_guessed): 
#   for i in range(0, len(letters_guessed)):
#     if letters_guessed[i] not in secret_word:
#       return False
#   return True

  for letter in secret_word:
      if letter not in letters_guessed:
        return False
  return True


# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

# secret_word = 'spie'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(is_word_guessed(secret_word, letters_guessed) )




#%%
# Create a function 1B) Getting the user’s guess
# function get_guessed_word that takes in two parameters a string, 
# secret_word , and a list of letters, letters_guessed. 
# This shouldn't be too different from is_word_guessed !
# want to get the word guessed
# created number of spaces with the number of letters in secret word
# loop to compare one element in letters_guessed vs secret_word
# if they are the same - then we temp store it in templist
#

# Next, implement the function get_guessed_word that takes in two parameters a string, 
# secret_word , and a list of letters, letters_guessed. This function returns a string 
# that is comprised of letters and underscores

# >>> secret_word = 'apple'
# >>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(get_guessed_word(secret_word, letters_guessed) )
# '_ pp_ e'


def get_guessed_word(secret_word, letters_guessed):
  # temp_list = ["_"] * (len(secret_word))
  # temp = ""
  # for letter in secret_word:
  #   temp = temp + "_" + " "

  # for i in range(0, len(letters_guessed)):
  #   for j in range(0, len(secret_word)):
  #     if letters_guessed [i] == secret_word [j]:
  #       temp_list[j]= secret_word [j]

  # #
  # return temp_list
  if(is_word_guessed(secret_word, letters_guessed)):
    return secret_word
  else:
    result = ""
    for letter in secret_word:
      if letter in letters_guessed:
        result += letter
      else:
        result += " _ "
    return result




# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

# secret_word = 'spie'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed) )
  
    

#%%
# Create a function 1C) Getting all available letters
# get_available_letters that takes in one parameter a list of letters,
#  letters_guessed.
#  returns a string that is comprised of lowercase English letters all lowercase 
# English letters that are not in letters_guessed. 
# This function should return the letters in alphabetical order.
# For this function, you may assume that all the letters in letters_guessed are lowercase.
# we want the alphabest 
# set so the letters are not repeated
# then we sorted it - these will be alphabetic. Return the list of letter minus what guessed so far

# Next, implement the function get_available_letters that takes in one parameter 
# a list of letters, lett
# ers_guessed . This function returns a string that is comprised of
#  lowercase English letters all lowercase English letters that are not in letters_guessed 

def get_available_letters(letters_guessed):
  my_ascii_set = set(string.ascii_lowercase)
  return "".join(sorted(my_ascii_set.difference(letters_guessed)))

  # bank_alpha = string.ascii_lowercase
  # for letter in letters_guessed:
  #   bank_alpha = bank_alpha.replace(letter, "")
  # return bank_alpha
  
# letters_guessed = ["a","b","c"]
# print(get_available_letters(letters_guessed))


#%%
# comparing the my_word vs the hint
# removing the space undoing the spacing
# if the hints are not the correct length so looking for length return false
# so if correct length then underscores and letters if they are not equal also return false
# 

# Now that you have built some useful functions, you can turn to implementing the function hangman ,
# which takes one parameter the secret_word the user is to guess. Initially, you can (and should!) 
# manually set this secret word when you run this function – this will make it easier to test your code. 
# But in the end, you will want the computer to select this secret word at random before inviting you or 
# some other user to play the game by running this function.
# Calling the hangman function starts up an interactive game of Hangman between the user and the computer. 
# In designing your code, be sure you take advantage of the three helper functions,
#  is_word_guessed , get_guessed_word , and get_available_letters , that you've defined in the previous part!

# 1.	The computer must select a word at random from the list of available words that was provided in words.txt. 
# The functions for loading the word list and selecting a random word have already been provided for you in hangman.py.
# 2.	Users start with 6 guesses.
# 3.	At the start of the game, let the user know how many letters the computer's word contains 
# and how many guesses s/he starts with.
# 4.	The computer keeps track of all the letters the user has not guessed so far and before each turn shows 
# the user the “remaining letters”


# def hangman(secret_word):
#   letters_guessed = []
#   available_letters = []
#   num_guesses = 6
#   num_warnings = 3
#   vowels = ["a","e","i","o","u"]

#   print("Welcome to the game Hangman!")
#   print(f"I am thinking of a word that is {len(secret_word)} letters long.")
#   print("-------------")
#   print('_ ' * len(secret_word))

#   while num_guesses > 0:
#     print(f"You have {num_guesses} guesses left.")
#     print(f"Available letters: {get_available_letters(letters_guessed)}")
#     guessed_letter = input("Please guess a letter: ")
#     guessed_letter = str.lower(guessed_letter)
#     if(num_warnings <= 0):
#       num_guesses -= 1
#       num_warnings = 0
#     if not guessed_letter.isalpha():
#       if(num_warnings > 0):
#         num_warnings -= 1
#         print(f"Oops! That is not a valid letter. You have {num_warnings} warnings left: {get_available_letters(letters_guessed)}")
#         print("-------------")
#       continue
#     if guessed_letter in letters_guessed:
#       if(num_warnings > 0):
#         num_warnings -= 1
#       print(f"Oops! You've already guessed that letter.. \nYou have {num_warnings} warnings left: {get_available_letters(letters_guessed)}")
#       print("----------------")
#       continue
#     else:
#       letters_guessed.append(guessed_letter)
#     if guessed_letter in secret_word:
#       print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
#       print("----------------")
#       num_guesses += 1
#       if(is_word_guessed(secret_word, letters_guessed)):
#         print("Congratulations, you won")
#         print("Your total score for this game is : ", num_guesses*len(set(secret_word)))
#         return
#       continue
#     else:
#         print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
#         if(letters_guessed in vowels):
#           num_guesses -= 1
#         else:
#           num_guesses -= 1
#         # num_guesses -= 1
#   print("Sorry, you ran out of guesses. The word was ", secret_word)


def match_with_gaps(my_word, other_word):
  other_word = other_word.replace(' ', '')
  other_word = str.lower(other_word)
  my_word = my_word.replace(' ', '')
  my_word = str.lower(my_word)

  if len(my_word) != len(other_word):
    return False
  
  for i in range(0, len(other_word)):
    if(my_word[i] == '_'):
      continue
    elif(my_word[i] != other_word[i]):
      return False
    elif(my_word.count(my_word[i]) != other_word.count(other_word[i])):
      return False

  return True

def show_possible_matches(my_word):
  my_set = []
  results =""

 # word_list = load_words()

  word_list = load_words(silent=True)
  for word in word_list:
    if(match_with_gaps(my_word, word)):
      my_set.append(word)
  if(len(my_set) == 0):
    print("No mathes found")
  else:
    for match in my_set:
      results += match + " "
    print("Possible word matches are:")

    print(results)
  return my_set



def hangman_with_hints(secret_word):
  letters_guessed = []
  available_letters = []
  num_guesses = 6
  num_warnings = 3
  vowels = ["a","e","i","o","u"]

  print("Welcome to the game Hangman!")
  print(f"I am thinking of a word that is {len(secret_word)} letters long.")
  print("-------------")
  print('_ ' * len(secret_word))

  while num_guesses > 0:
    print(f"You have {num_guesses} guesses left.")
    print(f"Available letters: {get_available_letters(letters_guessed)}")
    guessed_letter = input("Please guess a letter: ")
    guessed_letter = str.lower(guessed_letter)
    if(guessed_letter == '*'):
      #show_possible_matches(letters_guessed)
      temp = get_guessed_word(secret_word, letters_guessed)
      show_possible_matches(temp)
      #show_possible_matches(get_guessed_word(secret_word, letters_guessed))
    if(num_warnings <= 0):
      num_guesses -= 1
      num_warnings = 0
    if not guessed_letter.isalpha() and guessed_letter != '*':
      if(num_warnings > 0):
        num_warnings -= 1
        print(f"Oops! That is not a valid letter. You have {num_warnings} warnings left: {get_available_letters(letters_guessed)}")
        print("-------------")
      continue
    if guessed_letter in letters_guessed and guessed_letter != '*':
      if(num_warnings > 0):
        num_warnings -= 1
      print(f"Oops! You've already guessed that letter.. \nYou have {num_warnings} warnings left: {get_available_letters(letters_guessed)}")
      print("----------------")
      continue
    else:
      letters_guessed.append(guessed_letter)
    if(guessed_letter in vowels):
      num_guesses -= 2
      # print ("im in a vowel loop")
    else:
      num_guesses -= 1
        # # num_guesses -= 1
    
    if guessed_letter in secret_word:
      print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
      print("----------------")
      if (num_guesses != 6): # add to not increase the number of guesses
        num_guesses += 1
      
      if(is_word_guessed(secret_word, letters_guessed)):
        print("Congratulations, you won!")
        print("----------------")
        print("Your total score for this game is : ", num_guesses*len(set(secret_word)))
        print("----------------")
        return
      continue
    elif guessed_letter != '*':
        print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        print("----------------")
  print("Sorry, you ran out of guesses. The word was ", secret_word)
  print("----------------")


secret_word = choose_word(wordlist)
# hangman(secret_word)

hangman_with_hints(secret_word)






















  # num_guesses = 10
  # num_warnings = 3
  # spaces = '_ ' * len(secret_word)
  # letters_guessed = []
  # vowels = 'aeiou'

  # print("Welcome to the game Hangman!")
  # print(f"I am thinking of a word that is {len(secret_word)} letters long.")
  # print("-------------")
  
  # while num_guesses > 0:
  #   guessed_letter = input("Please guess a letter: ")
  #   guessed_letter = str.lower(guessed_letter)
  #   warnings_deducted = False

  #   if guessed_letter.isalpha() != True:
  #     num_warnings -= 1
  #     warnings_deducted = True

  #     if num_warnings <= 0:
  #       num_warnings = 0
  #       warnings_deducted = False
  #     print(f"Oops! That is not a valid letter. You have {num_warnings} warnings left: {get_available_letters(letters_guessed)}")

  #   if (guessed_letter in letters_guessed):
  #     num_warnings -= 1
  #     warnings_deducted = True

  #     if num_warnings <= 0:
  #       num_warnings = 0
  #       warnings_deducted = False
  #       should_deduct = True
  #     print(f"Oops! You've already guessed that letter.. \nYou have {num_warnings} warnings left: {get_available_letters(letters_guessed)}")

  #   if ((guessed_letter in vowels) and (not guessed_letter in letters_guessed) and (not guessed_letter in secret_word)):
  #     num_guesses -= 1
      
  #   if(warnings_deducted == False and should_deduct):
  #     num_guesses -= 1
  #     warnings_deducted = True

  #   print("guessed letter is: " + guessed_letter)
  #   letters_guessed.append(guessed_letter) 
  #   spaces = get_guessed_word(secret_word, letters_guessed)
  #   print("-------------")
  #   print(f"You have {num_guesses} guesses left.")
  #   print(f"Available letters: {get_available_letters(letters_guessed)}")
    
  #   if (guessed_letter in secret_word) and (not guessed_letter in letters_guessed):
  #     # num_warnings += 1
  #     print("Good guess: " + spaces)
  #     if is_word_guessed(secret_word, letters_guessed):
  #       print("Congratulations")
  #       return
  #   else:
  #     print("Oops! That letter is not in my word:" + spaces)
    
  
  # print("letters guessed list: " + "".join(letters_guessed))


# hangman("wordlist")
# print("This is what chooseword does to our word", choose_word("word"))