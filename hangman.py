# assignment: programming assignment 1
# author: Lynelle Goh
# date: 10/6/2022
# file: hangman.py is a program that will play a game of Hangman with the user
# input: size of a word to be guessed, number of lives, letters
# output: Hangman game where the user could win or lose

from distutils.errors import LibError
from random import choice, random

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    try:
      for line in open(filename):
        if len(line.strip()) == 13:
          dictionary.setdefault((12), []).append(line.strip())
        elif len(line.strip()) == 14:
          dictionary.setdefault((12), []).append(line.strip())
        elif len(line.strip()) == 12:
          dictionary.setdefault((12), []).append(line.strip()) 
        #https://www.w3schools.com/python/ref_dictionary_setdefault.asp
        #https://www.w3schools.com/python/ref_list_append.asp
        else:
          dictionary.setdefault(len(line.strip()), []).append(line.strip())
    except Exception:
        print('Wrong!')
    if 2 in dictionary:
      dictionary.pop(2)
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    pass 

  

# print out statement that you've already chosen this letter
def already_chosen ():
    print("You have already chosen this letter.")


# MAIN

if __name__ == '__main__' :


    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)


    # print the dictionary (use only for debugging)
    print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary


    # print a game introduction
    print("Welcome to the Hangman Game!")

    random_list = [3,4,5,6,7,8,9,10,11,12]
    outside = 0

    # START MAIN LOOP (OUTER PROGRAM LOOP)
      # set up game options (the word size and number of lives)
    def main():
      play = "Y"

      win = 0

      while play == "Y":
        choose = input("Please choose a size of a word to be guessed [3 – 12, default any size]:\n")
      
        try:
          if choose == "" or int(choose) < 3 or int(choose) > 12:
            print("A dictionary word of any size will be chosen.\n")
            number = choice(random_list)
            outside = 1
          elif choose.isnumeric():
            number = int(choose)
            outside = 0
        except:
          print("A dictionary word of any size will be chosen.\n")
          number = choice(random_list)
          outside = 1

        if (number >= 3 and number <= 12) and outside == 0:
          print('The word size is set to ' + str(number) + '.')
        elif number == 1 or number ==2 or number > 12:
          print("A dictionary word of any size will be chosen.")

        life_number = input("Please choose a number of lives [1 – 10, default 5]:\n")

        try:
          if life_number == "" or int(life_number) > 10 or int(life_number) < 1:
            print ("You have 5 lives.")
            life_number = 5
          elif life_number.isnumeric():
            print("You have " + life_number + " lives.")
            life_number = int(life_number)
        except:
          print ("You have 5 lives.")
          life_number = 5

      # select a word from a dictionary (according to the game options)
      # https://www.geeksforgeeks.org/python-check-whether-given-key-already-exists-in-a-dictionary/
        if number in dictionary.keys():
          select = dictionary[number]
          selection = choice(select)
          
      # use choice() function that selects an item from a list randomly, for example:
      # mylist = ['apple', 'banana', 'orange', 'strawberry']
      # word = choice(mylist)
      
          # START GAME LOOP   (INNER PROGRAM LOOP)
          
          while win == 0:
            print('Letters chosen:')
            selection_length = (len(selection))
            underscore = []
            word_into_string = []
            O_amount = []
            # death count
            death =  0
            chosen_already_again = 0
            # TA notes
            # space = ""
            # loop through the word (that youre guessing), looking every letter
                # check if the letter is in letters (has been seen already)
                # space += letter "_ " + "A" -> "_ A"
                # else
                  # space += "_ " "_ A" + "_ " -> "_ A _"

            # b a t
            # letter = ["a"]
            # b , b not in letters, space = "_"
            # a, a is in letters, space = "_ A"
            # t, t not in letters, space = "_ A _"


            # create the amount of underscores needed
            i = 0
            for i in range((selection_length)):
              if i == '-':
                underscore.append('-')
              else:
                underscore.append("__")
            

            # amount of lives being indicated with O
            for o in range((life_number)):
              O_amount.append("O")


            # print out correct amount of underscores
            for x in range(len(underscore)):
              print(underscore[x], end = "  ")

            
            # print out lives after letters
            print(' lives: ' + str(life_number), end=' ')
            for x in range(len(O_amount)):
              print(O_amount[x], end = "")


            # put all letters of word into a string
            for l in selection:
              word_into_string.append(l)


            # list of chosen letters already
            uppercase = []
            

            # game will continue if lives do not equal 0
            # game will continue if there are still underscores in list
            while int(life_number) != 0:
              if "__" in underscore:

                # inputting in a new letter
                guess = (input("\nPlease choose a new letter >\n"))

                # the guessed letter was in the word
                if guess.lower() in selection:
                  if guess.upper() not in uppercase:
                    chosen_already_again = 0
                    print("You guessed right!")
                    uppercase.append(guess.upper())
                    for index, e in enumerate(selection): # TA notes -> (0, b), (1, a), (2, t)
                      # if e == guess.lower():
                      #   underscore[index] = guess.upper()
                      if e == guess.lower():
                        underscore[index] = guess.upper()
                  elif guess.upper() in uppercase:
                    already_chosen()
                    chosen_already_again = 1


                else:
                  # what to do if letter is wrong
                  if guess.upper() in uppercase:
                    already_chosen()
                    chosen_already_again = 1
                  elif guess.lower() not in selection:
                    print("You guessed wrong, you lost one life.")
                    life_number = int(life_number) - 1
                    chosen_already_again = 0

                    # change the first O it sees into an X
                    O_amount[death] = 'X'
                    death = 1 + death

                    uppercase.append(guess.upper())

                    # person loses game
                    if life_number == 0:
                      print('You lost! The word is ' + selection.upper() + '!')
                      again = input("Would you like to play again [Y/N]?\n")
                      if again.upper() == "Y":
                        play = "Y"
                        win = 0
                        main()
                        
                        
                      else:
                        print("Goodbye!")
                        play = "N"
                        win = 1
                        chosen_already_again = 1
                        life_number = 0
                        break
                        

                if win == 0:    
                  # check if letter is already choose, if not, print everything
                  if chosen_already_again == 0:
                    print("Letters chosen: ", end="")  
                      
                    # print out letters that have already been chosen
                    print(', '.join(uppercase))


                    # print out new underscores
                    for x in range(len(underscore)):
                      print(underscore[x], end = "  ")


                      # print out lives
                    print(' lives: ' + str(life_number), end=' ')
                    for x in range(len(O_amount)):
                      print(O_amount[x], end = "")
                  
              else:
                print("\nCongratulations!!! You won! The word is " + selection.upper() + "!")
                again = input("Would you like to play again [Y/N]?\n")
                if again.upper() == "Y":
                  play = "Y"
                  win = 0
                  main()
                  
                  
                else:
                  print("Goodbye!")
                  play = "N"
                  win = 1
                  chosen_already_again = 1
                  life_number = 0
                  break
    main()