'''
Programmer: Jason Lunder
Class: CPSC 323-01, Fall 2021
Project #4 - Blocks world
9/30/2021

Description:
    This is a player object for the blocks world that can move blocks between locations and can tell the board to update to the next turn. It keeps track of whether or not it has won as well.
'''
from world import BlockWorld
import random

class Player:
    def __init__(self, world):
        self.world = world
        self.won = False

    def choose_move(self): 
        """
        Randomly select a move from the list of legal moves and apply it

        Parameters

        ----------

        Returns

        """
        moves = self.world.valid_moves()
        chosen_move = moves[random.randint(0, len(moves)-1)]
        self.world.move_block(chosen_move[0], chosen_move[1])

    def update(self):
        """
        Transition the board into the next turn state by making a move and checking for victory conditions

        Parameters

        ----------

        Returns

        Whether the player has won on this turn
        """
        self.choose_move()
        self.won = self.world.check_victory_condition()
        return self.won
