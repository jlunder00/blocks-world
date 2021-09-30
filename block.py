'''
Programmer: Jason Lunder
Class: CPSC 323-01, Fall 2021
Project #4 - Blocks world
9/30/2021

Description:
    This is a class that represents a block. A block has an id number and a record of whether or not it is covered. It can be covered or uncovered, or represented as a string
'''

import random

class Block:
    
    def __init__(self, id_num, uncovered):
        self.id_num = id_num
        self.uncovered = uncovered

    def cover(self):
        self.uncovered = False

    def uncover(self):
        self.uncovered = True

    def __str__(self):
        return str(self.id_num)+' '
