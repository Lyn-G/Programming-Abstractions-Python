# assignment: programming assignment 2
# author: Lynelle Goh
# date: 11/16/2022
# file: player.py controls and holds information about each character playing, such as either the AI or the user
# input: the diffent function intake different things, such as the player's name and their respective sign, or the updated board
# output: this program will output the player's sign, name, and placement on the board 
import random

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
             # all our valid choices
      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            print(self.name , ", " , self.sign , ": Enter a cell [A-C][1-3]:", sep='')
            asking = input()
            
            # combine both the uppercase letter and the number
            cell = asking[0].upper() + asking[1]
             
            # check if it is in our valid cells
            while board.isempty(cell) == False:
                  print("You did not choose correctly.")
                  print(self.name , ", " , self.sign , ": Enter a cell [A-C][1-3]:", sep='')
                  asking = input()
                  cell = asking[0].upper() + asking[1]
            
            # if it's true, mark the cell
            if board.isempty(cell) == True:
                  board.set(cell, self.sign)

class AI(Player):
      def __init__(self, name, sign, board):
            self.name = name
            self.sign = sign

      # randomly choose a cell
      def choose(self, board):
            self.validCells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            choosing = random.choice(self.validCells)

            print(self.name , ", " , self.sign , ": Enter a cell [A-C][1-3]:", sep='')

            # check if cell is valid, if not continuously randomly choose
            while board.isempty(choosing) == False:
                  choosing = random.choice(self.validCells)
            
            # once cell is valid, set it 
            if board.isempty(choosing) == True:
                  print(choosing)
                  board.set(choosing, self.sign)
                  