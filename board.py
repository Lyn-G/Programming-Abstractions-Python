# assignment: programming assignment 2
# author: Lynelle Goh
# date: 11/16/2022
# file: board.py creates the board needed for the program and has functions that check specific values about the board, such as size or if it's empty
# input: this program accepts many different inputs for different functions, such as the cell location and the player's sign
# output: this program outputs different things, such as setting a marker in the correct position, setting up the board, returning a boolean for a winner
#           if conditions are met, and more
class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3 # creates " " * 9
            self.board = list(self.sign * self.size**2) # [ , , , , , , , , ]
            self.validCells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

            # the winner's sign O or X
            self.winner = ""

      def get_size(self): 
             # optional, return the board size (an instance size)
             pass

      def get_winner(self):
            # return the winner's sign O or X (an instance winner)   
             return self.sign  

      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you 

            index = self.validCells.index(cell)
            self.board[index] = sign

      def isempty(self, cell):
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)

            index = self.validCells.index(cell)
            if self.board[index] == ' ':
                  return True
            else:
                  return False

      def isdone(self):
            done = False
            self.winner = ''
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            
            # checking rows for winning
            if (('X' == self.board[0]) and ('X' == self.board[3]) and ('X' == self.board[6])):
                  done = True
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[0]) and ('O' == self.board[3]) and ('O' == self.board[6])):
                  done = True
                  self.sign = 'O'
                  return self.sign
            elif (('X' == self.board[1]) and ('X' == self.board[4]) and ('X' == self.board[7])): 
                  done = True
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[1]) and ('O' == self.board[4]) and ('O' == self.board[7])):
                  done = True
                  self.sign ='O'
                  return self.sign
            elif (('X' == self.board[6]) and ('X' == self.board[7]) and ('X' == self.board[8])): 
                  done = True
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[6]) and ('O' == self.board[7]) and ('O' == self.board[8])):
                  done = True
                  self.sign = 'O'
                  return self.sign
            
            # checking columns for winning
            elif (('X' == self.board[0]) and ('X' == self.board[1]) and ('X' == self.board[2])): 
                  done = True
                  print(self.sign , 'Hello!')
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[0]) and ('O' == self.board[1]) and ('O' == self.board[2])):
                  done = True
                  self.sign = 'O'
                  return self.sign
            elif (('X' == self.board[3]) and ('X' == self.board[4]) and ('X' == self.board[5])): 
                  done = True
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[3]) and ('O' == self.board[4]) and ('O' == self.board[5])):
                  done = True
                  self.sign = 'O'
                  return self.sign
            elif (('X' == self.board[6]) and ('X' == self.board[7]) and ('X' == self.board[8])): 
                  done = True
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[6]) and ('O' == self.board[7]) and ('O' == self.board[8])):
                  done = True
                  self.sign = 'O'
                  return self.sign

            # checking diagonals for winning
            elif (('X' == self.board[0]) and ('X' == self.board[4]) and ('X' == self.board[8])): 
                  done = True
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[0]) and ('O' == self.board[4]) and ('O' == self.board[8])):
                  done = True
                  self.sign = 'O'
                  return self.sign
            elif (('X' == self.board[2]) and ('X' == self.board[4]) and ('X' == self.board[6])):
                  done = True
                  self.sign = 'X'
                  return self.sign
            elif (('O' == self.board[2]) and ('O' == self.board[4]) and ('O' == self.board[6])):
                  done = True
                  self.sign = 'O'
                  return self.sign
            elif ' ' not in self.board:
                  done = False
                  return self.sign
            
      def show(self):
            # print out the current board
            print("   A   B   C")
            print(" +---+---+---+")
            print("1|", self.board[0] ,"|" , self.board[3],  "|" , self.board[6], "|")
            print(" +---+---+---+")
            print("2|", self.board[1] ,"|" , self.board[4],  "|" , self.board[7], "|")
            print(" +---+---+---+")
            print("3|", self.board[2] ,"|" , self.board[5],  "|" , self.board[8], "|")
            print(" +---+---+---+")
