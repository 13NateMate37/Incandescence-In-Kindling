"""
This file contains the imports and functions for Stat Array Generation.


Contents: 

1)    SAG-4d6d1 - Function for returning an array of 6 stats via rolling 4d6d1 
2)    SAG-Std   - Function for returning an array of 6 stats via Standard Array, 15,14,13,12,10,8
3)    SAG-PB - Function for returning a base array of 6 8's for Point Buy spending
3a1)  Point Buy cost logic as a dictionary
3a2)  Logic for Point Buy. Sets the budget of spendable points. To be linked to difficulty.
3a3)  Logic for assigning a stat to an ability score.
3b)   Function for user to select a Point Buy budget   
4)    Function for user to select a Stat Generation Method.
"""

from dice import roll_4d6_drop_lowest


# 1 SAG-4d6d1
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
        rolls = roll_4d6_drop_lowest()
        # Add to results
        results.append(rolls)
    # Return the array sorted
    return sorted(results, reverse=True)



# 2 SAG-Std
# Returns standard array values
def array_roller_standard():
    # Declaring array values
    standard_array = [15, 14, 13, 12, 10, 8]
    return standard_array



# 3 SAG-PB
# Returns the base Point Buy Array of 6 8's
def array_roller_point_buy():
    # Declaring array values
    point_buy_array = [8, 8, 8, 8, 8, 8]
    return point_buy_array



# 3a_1
# Point Buy costs in Dictionary form
Point_Buy_Costs = {
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



# 3a_2
# Campaign Budget Dictionary
Campaign_Budget = {
            "Low Fantasy": 10,
            "Standard Fantasy": 15,
            "High Fantasy": 25,
            "Epic Fantasy": 30
}



# 3a_3
# Ability Score, Blank Dictionary
Ability_Scores = {
    "Strength": None,
    "Dexterity": None,
    "Constitution": None,
    "Intelligence": None,
    "Wisdom": None,
    "Charisma": None
}



# 3b
# Select campaign budget 
def select_budget():
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


# 4 SAG_MethodPicker
# Let's the user choose their array method
def choose_array_method():
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



def assign_ability_scores(stat_array: list, Ability_Scores: dict):
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
    for Ability in assign_ability_scores:
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

