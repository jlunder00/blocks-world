'''
Programmer: Jason Lunder
Class: CPSC 323-01, Fall 2021
Project #4 - Blocks world
9/30/2021

Description:
    This is the driver program for blocks world. It instantiates a player and world with random parameters for the number of blocks and the number of locations, and runs the game until the player wins.
'''

from player import Player
from world import BlockWorld
import random

def start():
    """
    Begin the game

    Parameters

    ----------

    Returns

    """
    player = Player(BlockWorld(random.randint(3, 10), random.randint(3, 10)))
    run(player)

def run(player):
    """
    Run each turn of the game and show its board state at each turn

    Parameters

    ----------

    Returns

    """
    while player.won != True:
        player.update()
        player.world.show()
    print('Player won!')

if __name__ == '__main__':
    start()
