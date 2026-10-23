"""
Stat_Array_Generation.py

This file contains the functions for generating stat arrays and the accomanying logic.

Takes imports from:
Dice.py

Contents: 

1) Import Block:    ImpBlk 
2) Globals:  
            Gbl-1a - Ability score dictionairy for mapping values too
            Gbl-2a - Campaign budget dictionairy for pointbuy games
            Gbl-2b - Pointbuy score cost values, in ScoreValue: AmountOFPoints,
                     (With -x effectively giving more points)
3) Stat Array Generation:
            SAG-1a: arry_Roller_4d6d1 - Returns an array using the 4d6d1 rolling method
            SAG-1b: arry_Roller_Standard - Returns an array of the Standard method 
            SAG-1c: arry_Roller_Pointbuy - Returns an array of 8's for later point spending
4) User Choice Selection:
            UCS-1a: choose_Array_Method - Allows user to choose SAG method
            UCS-1b: choose_Campaign_Budget - Allows user to choose a Pointbuy total 
5) Ability Score Assignment:
                ASA-1a: assign_Ability_Scores - Allows user to pick which value they want to
                         assign to each ability score
                ASA-1b: spend_Pointbuy_Points - Allows user to modulate their ability score 
                         values.
"""




# ImpBlk
from Dice import roll_4d6_Drop_Lowest




# Gbl-1a
# Ability Score, Blank Dictionary
ABILITY_SCORES_BLANK_BASE = {
    "Strength": None,
    "Dexterity": None,
    "Constitution": None,
    "Intelligence": None,
    "Wisdom": None,
    "Charisma": None
}

# Gbl-2a
# Campaign Budget Dictionary
CAMPAIGN_BUDGETS = {
            "Low Fantasy": 10,
            "Standard Fantasy": 15,
            "High Fantasy": 25,
            "Epic Fantasy": 30
}

# Gbl-2b
# Point Buy costs in Dictionary form
POINTBUY_POINT_COSTS = {
    7: -4,
    8: -2,
    9: -1,
    10: 0,
    11: 1,
    12: 2,
    13: 3,
    14: 5,
    15: 7,
    16: 10,
    17: 13,
    18: 17
}




# SAG-1a
def array_Roller_4d6d1():
    """
    Rolls 4d6 and drops the lowest die six times.
    Returns a list of the six results.
    """
    # Store result into variable
    results = []
    # Roll 6 times to make an array of 6
    for _ in range(6):
        rolls = roll_4d6_Drop_Lowest()
        # Add to results
        results.append(rolls)
    # Return the array sorted
    return sorted(results, reverse=True)


# SAG-1b
def array_Roller_Standard():
    # Declaring array values
    standard_array = [15, 14, 13, 12, 10, 8]
    return standard_array


# SAG-1c
def array_Roller_Pointbuy():
    # Declaring array values
    point_buy_array = [8, 8, 8, 8, 8, 8]
    return point_buy_array




# UCS-1a 
def choose_Array_Method():
    """
    User select's their desired method for Stat Array Generation. 
    Will call the corresponding SAG function
    """

    # Mapping the choices 
    choices = {
        1: "Standard Array",
        2: "4d6d1",
        3: "Point Buy"
    }

    # Printed message 
    prompt = (
        "Please select an Array Method"
        "\n 1) Standard Array\n 2) 4d6d1"
        "\n 3) Point Buy\n"
    )

    # Loops if 1-3 isn't entered
    # Loops if non numerical
    while True:
        try:
            selected_method = int(input(prompt))
        except ValueError:
            print("Please enter a number from 1 to 3.")
            continue

        # Loops is a number not 1-3 is chosen
        if selected_method in choices:
            return choices[selected_method]

        print("Please enter a number from 1 to 3.")


# UCS-1b
def choose_Campaign_Budget():
    """
    User select's their campaign budget. Larger budget's
    being harder difficulties.
    """

    # Print a warning
    print("Warning! As the budget increases,\n So does the difficulty!")

    # Mapping the choices 
    choices = {
        1: "Low Fantasy",
        2: "Standard Fantasy",
        3: "High Fantasy",
        4: "Epic Fantasy",
    }

    # Printed message 
    prompt = (
        "Please select Fantasy Budget."
        "\n 1) Low (10pts)\n 2) Standard (15pts)"
        "\n 3) High (24 pts)\n 4) Epic (30 pts)\n"
    )

    # Loops if 1-4 isn't entered6
    # Loops if non numerical
    while True:
        try:
            selected_budget = int(input(prompt))
        except ValueError:
            print("Please enter a number from 1 to 4.")
            continue

        # Loops is a number not 1-4 is chosen
        if selected_budget in choices:
            return choices[selected_budget]

        print("Please enter a number from 1 to 4.")




# ASA-1a
def assign_Ability_Scores(stat_array: list, Ability_Scores: dict):
    """
    This function takes a Stat Array (as a list) and te blank Ability_Scores
    dictionary as input, allowing the user to manual assign values from their
    Stat Arrays to the desired Ability Score. Resulting in a new dictionary.
    """

    # Making a copy of the Ability_Scores dictionary
    assigned_scores = Ability_Scores.copy()
    # Same for the remaining scores
    remaining_scores = stat_array.copy()

    # For each Ability Sore in the dictionary, top down
    for Ability in assigned_scores:
        # Loop setup to move through all 6 scores
        while True:
            # Show what values are left to assign
            print(f"Ability Scores left: {remaining_scores}")
            # Capture user input for the current Ability Score
            choose_score = input(f"Choose a value for {Ability}:\n")

            # Establishing try/except block
            try:
                # Convert the captured str to an int 
                chosen_score = int(choose_score)
            # If can't due to not being a recognised whole number
            except ValueError:
                print("Choose a value from your Stat Array")
                continue # Return to the loop start

            # checking if the user made up a value
            if chosen_score not in remaining_scores:
                # print a reminder and return to the loop start
                print("Choose a value from your Stat Array")
                continue

            # Assigning the Value to the Key
            assigned_scores[Ability] = chosen_score
            # Removing it from the selection
            remaining_scores.remove(chosen_score)
            # breaking the loop
            break
    return assigned_scores

# ASA-1b
def spend_Pointbuy_Points():
    