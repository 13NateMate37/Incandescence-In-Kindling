"""
Dice.py

This file contains the funtions needed for rolling dice.

Takes imports from:
native random module

Contents:

1) Import Block:
            ImpBlk
2) Dice Roll Fucntions:
            DRF-1a: roll_Dice - Basic random number generation, mimicing a die.
            DRF-1b: roll_4d6_Drop_Lowest - Shortcut function for matching SAG funciton
"""



# ImpBlk
import random




# DRF-1a
def roll_Dice(amount_of_dice:int, sides:int):
    """
    Simulates rolling dice. Takes the amount of dice and type of dice as parameters.
    Can only roll one die division at a time, i.e. 4d6, 2d20, 1d12, etc.  
    """
    # Initialising an empty list to store the result
    results = []
    # Repeat times equal to amount_of_dice
    for _ in range(amount_of_dice):
        # Rolling the dice and appending the result to the list
        die_roll = random.randrange(1, sides+1)
        results.append(die_roll)
    # Return the value of results
    return results


# DRF-1b
def roll_4d6_Drop_Lowest():
    """
    Rolls 4d6 and drops the lowest die.
    Returns the sum of the remaining three dice.
    """
    # Main purpose, stored to variable
    rolls = roll_Dice(4, 6)
    # Remove the lowest roll
    rolls.remove(min(rolls))  
    # Sum the remaining values
    return sum(rolls)

