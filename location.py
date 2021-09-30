'''
Programmer: Jason Lunder
Class: CPSC 323-01, Fall 2021
Project #4 - Block world
9/30/2021

Description:
    This is a class representing a location in the block world. It has a list of the blocks it contains, keeps track of which block is on top, and has the ability to place a given block on its stack and remove one from the top of its stack.
'''
import block

class Location:

    def __init__(self):
        self.current_blocks = []
        self.top_block = None

    def place_block(self, block):
        """
        Place a given block on the top of the stack at this location

        Parameters

        ----------

        block : the block to place of type Block
        """
        if self.top_block != None:
            self.current_blocks[-1].cover()
            self.top_block = block
        self.current_blocks.append(block)

    def remove_block(self):
        """
        Remove the block on the stack at this location and return it

        Parameters

        ----------

        Returns

        The block removed from the top of the stack
        """
        block = self.current_blocks.pop()
        if len(self.current_blocks) > 0:
            self.current_blocks[-1].uncover()
            self.top_block = self.current_blocks[-1]
        else:
            self.top_block = None

        return block
