# Ability score list 
ability_score_names = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma"
    ]


def get_ability_score_data(ability_scores):
    # Initialise an empty dictionary to store the ability score data
    ability_data = {} 

    for ability_name, ability_score in ability_scores.items():
        ability_data[ability_name] = {
                "Score": ability_score,
                "modifier": calculate_modifier(ability_score)
        }
    return ability_data


# Calculate the modifier of a given ability score
def calculate_modifier(ability_score):
    """
    Calculates the modifier for a given ability score.
    """
    return (ability_score - 10) // 2


# Test print
# print(calculate_modifier(15)) 