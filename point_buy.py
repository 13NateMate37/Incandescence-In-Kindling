# Point Buy System for Character Creation

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

# Looks up the point buy cost for a given ability score total
def get_point_buy_cost(ability_score):
    """
    Returns the point buy cost for a given ability score.
    """
    return point_buy_costs[ability_score]


# Test print
# print(get_point_buy_cost(15))


def calculate_total_point_buy_cost(ability_scores):
    total_cost = 0

    for ability_score in ability_scores:
        total_cost += get_point_buy_cost(ability_score)

    return total_cost

# Test print
ability_scores = [15, 14, 13, 12, 10, 8]
print(calculate_total_point_buy_cost(ability_scores)) 