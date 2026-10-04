"""
This file contains the imports and functions for 4d6d1* Array Generation.
*Four d6's, dropping the lowest, summing the remaining three d6's 
"""


from dice import roll_dice

# Foundation funciton for array roller
def roll_4d6_drop_lowest():
    """
    Rolls 4d6 and drops the lowest die.
    Returns the sum of the remaining three dice.
    """
    # Main purpose, stored to variable
    rolls = roll_dice(4, 6)
    
    # Remove the lowest roll
    rolls.remove(min(rolls))  
    
    return sum(rolls)


# Creates an array of 6 stats
def array_roller_4d6d1():
    """
    Rolls 4d6 and drops the lowest die six times.
    Returns a list of the six results.
    """
    # Store result into variable
    results = []

    # Roll 6 times to make an array of 6
    for _ in range(6):
        result = roll_4d6_drop_lowest()
        results.append(result)

    # Return the array sorted
    return sorted(results, reverse=True)

# Test print
# print(array_4d6d1_roller())