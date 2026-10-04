"""

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

point_buy_budget = [20, 25, 30]

# Looks up the point buy cost for a given ability score total
def get_point_buy_cost(ability_score):
    """
    Returns the point buy cost for a given ability score.
    """
    return point_buy_costs[ability_score]


# Test print
# print(get_point_buy_cost(15))


# 'Point Buy' point totaller
def calculate_total_point_buy_cost(ability_scores):
    """
    Calculates the amount of Points spent on a stat array
    """
    total_cost = 0

    for ability_score in ability_scores:
        total_cost += get_point_buy_cost(ability_score)

    return total_cost


# Test print
# ability_scores = [15, 14, 13, 12, 10, 8]
# print(calculate_total_point_buy_cost(ability_scores)) 


def point_buy_validator(ability_scores, budget):
    """
    Validates spent points against the budget tier
    """
    total_cost = calculate_total_point_buy_cost(ability_scores)

    # Return whether the total cost is within the budget
    return total_cost <= budget


# # Test print
# ability_scores = [15, 14, 13, 12, 10, 8]
# print(calculate_total_point_buy_cost(ability_scores)) 
# print(point_buy_validator(ability_scores, 20))
# print(point_buy_validator(ability_scores, 10))


def legal_stat_checker(ability_score):
    """
    Checks if a given ability score is legal within the Point Buy system.
    """
    return ability_score in point_buy_costs


#TEst print
# print(legal_stat_checker(15)) 
# print(legal_stat_checker(19))  
# print(legal_stat_checker(20))

def validate_PB_stat_array(ability_scores, budget):
    """
    Validates the stat array for the Point Buy budget.
    """
    total_cost = calculate_total_point_buy_cost(ability_scores)
    return total_cost <= budget


