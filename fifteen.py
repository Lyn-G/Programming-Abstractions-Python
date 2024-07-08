# assignment: programming assignment 5
# author: Lynelle Goh
# date: 12/1/2022
# file: fifteen.py has many functions that help with setting up the game, running it, and ending it
# input: the functions in this file accept any type of numbers
# output: can produce a visual drawing of the Fifteen Game at any point, or updating the game and tile placement,
#       or check where the game is at by returnning true or false  

import numpy as np
from random import choice

class Fifteen:
    
    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        print(self.tiles)

    def update(self, move):
        pass

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space)  
    def transpose(self, i, j):
        pass

    # return a list of all adjacent tiles
    def adj(index):
        pass

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice (self.adj(index))
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
# checks if the move is valid: one of the tiles is 0 and another tile is its neighbor     
    def is_valid_move(self, move):
        pass
 # verify if the puzzle is solved
    def is_solved(self):

        counter = 0

        for i in range(15):
            if self.tiles[i] == i:
                counter += 1

        if counter == 15:
            return True

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        print('+-----+-----+-----+-----+')
        print('|', self.tiles[1], '|', self.tiles[2],'|', self.tiles[3],'|', self.tiles[4], '|')
        print('+-----+-----+-----+-----+')
        print('|', self.tiles[5], '|', self.tiles[6],'|', self.tiles[7],'|', self.tiles[8], '|')
        print('+-----+-----+-----+-----+')
        print('|', self.tiles[9], '|', self.tiles[10],'|', self.tiles[11],'|', self.tiles[12], '|')
        print('+-----+-----+-----+-----+')
        print('|', self.tiles[13], '|', self.tiles[14],'|', self.tiles[15],'|', self.tiles[16], '|')
        print('+-----+-----+-----+-----+')   

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15   
    def __str__(self):
        print(np.array2string(self.tiles))

    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''
    '''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    '''
    
    
        
