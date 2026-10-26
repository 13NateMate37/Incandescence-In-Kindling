# Incandescence In Kindling

This is a passion project for bring my own ideas to life while practicing coding and development.


## What is?

Working in Python, I will engineer game logic for a Table Top Role Playing Game. I have a peronsal setting I wish to work and have decided to do it through this medium. 

I will be using Streamlit to create a 'front-end' for the experience and will be using Ollama to run a local model AI as an interactive 'Game Master'.

Development is expected to slightly wonky to start with. streamlining as I start picking habbits and noticing patterns. 

This is semi-guided through the use of AI as a learning tool along side documentation and my previous Python basics training. 


## Development Roadmap

# Currently finished

*Dice.py*
- Basic die roll function 
- A setup function 4d6d1 for stat array function

*Stat_Generation_Array*
- Contains array_roller_XXXX funtions that return lists of 6 figures
- Dictionaries for the stat generation process. 
- Identical functions for array generation method and campaign budget if point buy 
- Function for assigning scores from the array to the Ability


# Working towards

- Need a funciton for spending Point Buy  points based upon the campaign budget.
  - Initialize a copy of the ability-score dictionary with all six scores at 10.
  - Call `choose_Campaign_Budget()` and use its returned campaign name to look up the custom point total in `CAMPAIGN_BUDGETS`.
  - Calculate the total cost from all six scores using `POINTBUY_POINT_COSTS`, then calculate the points remaining.
  - Display the current scores and points remaining each turn. Allow the player to enter an ability name to change its score.
  - Validate score input: require a whole number from 7 to 18, and explain invalid or non-numeric input before prompting again.
  - Confirm each proposed change. If confirmed, calculate the proposed total by replacing the old score's cost with the new score's cost.
  - Accept the change only if the proposed total does not exceed the selected budget; update the ability score, total cost, and remaining points only after it passes. Otherwise, explain that the change exceeds the budget.
  - Explain when a player declines a change, and keep the current scores and totals unchanged.
  - Require the player to spend the entire budget before entering `Done` to finish; if points remain, tell them how many are left. Return the completed ability-score dictionary when the budget is fully spent.
- Ability Score bonus checker 
- array_Roller_Pointbuy was decided to be redundant, refactoring logic flow 





