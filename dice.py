"""
This file contains the imports and funtions needed for rolling dice.
"""


import random


 #Core die rolling function
def roll_dice(amount_of_dice, sides):
    """
    Rolls dice. Takes the amount of dice and type of dice as parameters.
    Can only roll one die division at a time, i.e. 4d6, 2d20, 1d12, etc.  
    """
    # Initialising an empty list to store the result
    results = []
    
    for _ in range(amount_of_dice):
        # Rolling the dice and appending the result to the list
        result = random.randint(1, sides)
        results.append(result)

    return results

# Test print
# print(roll_dice(4, 6))

