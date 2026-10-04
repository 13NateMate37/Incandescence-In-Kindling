"""
This file contains the imports and functions for Stat Array Generation
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
        result = roll_4d6_drop_lowest()
        results.append(result)

    # Return the array sorted
    return sorted(results, reverse=True)


# 2 SAG-Std
# Returns standard array values
def array_roller_standard():
    # Declaring array values
    standard_array = [15, 14, 13, 12, 10, 8]
    return standard_array


# 3 SAG-PB

# 3a_1
# Point Buy costs in Dictionary form
point_buy_costs = {
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
# Campaign budgets
campaign_budget = {
            "Low Fantasy": 10,
            "Standard Fantasy": 15,
            "High Fantasy": 24,
            "Epic Fantasy": 30
}


# 3a_3
# Ability score
ability_scores = (
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma",
)

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

#

# Point Buy method to generate ability scores based on user input
def spend_points(budget):
    """
    Prompts the user to enter ability scores until the total cost matches the budget.
    
    Args:
        budget (int): The campaign budget in points.
        
    Returns:
        dict: A dictionary of selected ability scores.
    """
    point_buy_costs = {
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
    
    ability_scores = [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence",
        "Wisdom",
        "Charisma"
    ]
    
    scores = {}
    total_cost = 0
    
    for ability in ability_scores:
        while True:
            try:
                score = int(input(f"Enter {ability}'s score (7-18): "))
                if not (7 <= score <= 18):
                    raise ValueError("Score must be between 7 and 18.")
                
                points_needed = budget - total_cost + point_buy_costs[score]
                
                if points_needed >= 0:
                    scores[ability] = score
                    total_cost += point_buy_costs[score]
                    break
                else:
                    print("That score would make it impossible to spend the budget exactly. Choose another score.")
            except ValueError as e:
                print(e)
    
    return scores

# Function to generate ability scores using the selected method
def array_roller_point_buy():
    """
    Generates ability scores based on user selection.
    
    Returns:
        dict: A dictionary of selected ability scores.
    """
    budget = select_budget()
    selected_method = input("Select a method (4d6d1, Std, PB): ")
    
    if selected_method == "4d6d1":
        return array_roller_4d6d1()
    elif selected_method == "Std":
        return array_roller_standard()
    elif selected_method == "PB":
        return spend_points(budget)
    else:
        print("Invalid method selected. Please try again.")
        return None