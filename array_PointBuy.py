"""
This file conatins the imports and functions for Point Buy* Array Generation.
*Players stats start at 8 and have a budget of points to spend on increasing them, 
with the cost increasing as the stat increases.
"""


# Point Buy costs in Dictionary form
point_buy_costs = {
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


# Campaign budgets
campaign_budget = {
            "Low Fantasy": 10,
            "Standard Fantasy": 15,
            "High Fantasy": 24,
            "Epic Fantasy": 30
}


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


    
print(select_budget())
