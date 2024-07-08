# assignment: programming assignment 3
# author: Lynelle Goh
# date: 11/16/2022
# file: steganography.py is a program that takes in an image and is able to properly
#       encode or decode a secret message hidden in the RBG pixels of the image
# input: takes in an input from the driver code and executes encode, decode, print, or shows the image depending on what the user inputs
# output: depending based on what the user has inputted, this code will either encode the message inputted by the user into the selected image,
#       decode a message from the selected image, print out the message that was inputted, or show the image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    name = ''
    delimeter = ''

    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    
    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        # for debugging 
        # print(image)
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == 'huffman':
            self.codec = HuffmanCodes(delimiter = self.delimiter)
        binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message 
            self.binary = binary

            # access element in array and compare it with the binary string
            s = 0 # counter variable
            l = 0 # index variable
            for i in range(len(image)):
                for j in range(len(image[i])):
                    for k in range(len(image[i][j])):
                        if ((image[i][j][k] % 2) == 0): # check if even
                            if (binary[l] == '1'): # # check if it's 1
                                if image[i][j][k] == 0:
                                    image[i][j][k] = 1
                                    # print('even and 1')
                                else:
                                    image[i][j][k] = image[i][j][k] + 1
                        elif ((image[i][j][k] % 2) != 0 and binary[l] == '0'): # odd and 0
                            if image[i][j][k] == 1:
                                image[i][j][k] = 0
                            else:
                                image[i][j][k] = image[i][j][k] - 1
                        # for debugging
                        # print(image[i][j][k], binary[l], s)

                        # update s and l
                        s = s + 1
                        l = l + 1

                        # break out of these loops entirely
                        if s == (len(binary)):
                            break
                    if s == (len(binary)):
                            break
                if s == (len(binary)):
                            break
            cv2.imwrite(fileout, image) # changed question mark
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        # for debugging 
        # print(image)  

        flag = True
        binary_string = ''
        ending_binary = ''
        binary = []

        # convert into text
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # your code goes here
            # you may create an additional method that extract bits from the image array
            for i in range(len(image)):
                for j in range(len(image[i])):
                    for k in range(len(image[i][j])):
                        if ((image[i][j][k] % 2) == 0):
                            binary_string = binary_string + '0' # add 0 to the binary string if it's even
                        else:
                            binary_string = binary_string + '1' # add 1 to the binary string if it's odd
            binary_data = binary_string # changed question mark
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            for i in range(0,len(binary_data),8): # access the items in the binary data
                byte = binary_data[i: i+8] 
                if byte == self.codec.encode(self.delimiter):
                    binary.append('00100011') # added the delimiter binary number at the end of binary string data
                    break
                binary.append(byte)
            for x in range(len(binary)):
                ending_binary = ending_binary + binary[x] # access the list and add it to the string that needs to be printed
            self.binary = ending_binary # changed question mark              
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

