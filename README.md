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
  - Start with a copy of the blank ability-score dictionary and set all six scores to 8.
  - Call `choose_Campaign_Budget()` and use the returned campaign name to look up its numeric budget in `CAMPAIGN_BUDGETS`.
  - Calculate the total cost of all six current scores using `POINTBUY_POINT_COSTS`. Since the costs are cumulative relative to 10, six starting scores of 8 have a combined cost of -12.
  - Show the player their current scores, selected budget, combined cost, and remaining room under the budget.
  - Ask which ability score to change and what new score to assign. Validate that the ability is valid and the score is an integer listed in `POINTBUY_POINT_COSTS`.
  - Before applying a change, calculate the proposed combined cost. Accept the change only if it does not exceed the selected budget; otherwise, explain why and prompt again.
  - Repeat until the player chooses to finish, then return the completed ability-score dictionary. The player does not need to spend the entire budget.
  - Decide whether spending points only allows increasing scores or whether lowering scores can earn points; make that behavior explicit.
  - Resolve the High Fantasy budget mismatch: `CAMPAIGN_BUDGETS` currently specifies 25 points, while the selection prompt says 24.
- Ability Score bonus checker 
- array_Roller_Pointbuy was decided to be redundant, refactoring logic flow 






