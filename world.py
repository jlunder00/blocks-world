'''
Programmer: Jason Lunder
Class: CPSC 323-01, Fall 2021
Project #4 - Blocks world
9/30/2021

Description:
    This is an object representing the world that blocks live in. It has a set of locations and blocks distributed in those locations, according to the number of places and number of blocks passed in in the init function. It can add blocks to the world, generate a set of valid moves for the current board state, move blocks between locations, check to see if the victory conditions have been met and print a representation of the board.
'''

import random, location, block

class BlockWorld:

    def __init__(self, num_places, num_blocks):
        self.num_places = num_places
        self.num_blocks = num_blocks
        self.locations = [location.Location() for i in range(self.num_places)]
        self.add_blocks()
        while(self.check_victory_condition()):
            self.add_blocks()


    def add_blocks(self):
        """
        Add all of the blocks in the range of possible block ids to random locations in the block world

        Parameters

        ----------

        Returns

        """
        for i in range(self.num_blocks):
            j = random.randint(0, self.num_places-1)
            self.locations[j].place_block(block.Block(i, True))

    def move_block(self, oldLocation, newLocation):
        """
        Move a block from one location to another

        Parameters

        ----------

        oldLocation : the index within the locations list of the location to take the block from
        newLocation : the index within the locations list of the location to add the block to

        Returns
        
        """
        block_in_transit = self.locations[oldLocation].remove_block()
        self.locations[newLocation].place_block(block_in_transit)

    def valid_moves(self):
        """
        Generate all possible legal moves in the current position

        Parameters

        ----------

        Returns

        A list of all the possible moves as a list of tuples where the first index is the old location and the second is the new location
        """
        moves = []
        for i in range(len(self.locations)):
            if len(self.locations[i].current_blocks) == 0:
                continue
            for j in range(-1,2):
                if i+j > -1 and i+j < self.num_places and j != 0:
                    moves.append((i, i+j))
        return moves

    def check_victory_condition(self):
        """
        Evaluate the current board state to see if a victory condition has been met

        Parameters

        ----------

        Returns

        A boolean that is true if the board is in a win state and false otherwise
        """
        for location in self.locations:
            if len(location.current_blocks) == 0:
                continue
            
            if len(location.current_blocks) > 0 and len(location.current_blocks) != self.num_blocks:
                return False
            
            block_ids = [block.id_num for block in location.current_blocks]
            if sorted(block_ids) == block_ids:
                return True
            else:
                return False

    def show(self):
        """
        Print out the current board state

        Parameters

        ----------

        Returns
        
        """
        overall_print = [['N ' for j in range(0, self.num_places)] for i in range(0, self.num_blocks)]
        print('___________________________________')
        for i in range(self.num_blocks):
            for j in range(len(self.locations)):
                if i < (self.num_blocks-len(self.locations[j].current_blocks)):
                    overall_print[i][j] = 'N '
                else:
                    index = (i-(self.num_blocks-len(self.locations[j].current_blocks)))
                    overall_print[i][j] = str(self.locations[j].current_blocks[(len(self.locations[j].current_blocks)-1)-index])
        for i in range(len(overall_print)):
            for j in range(len(overall_print[i])):
                print(overall_print[i][j], end='')
            print()
        print('___________________________________')
            

