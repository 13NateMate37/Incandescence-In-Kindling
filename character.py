# Aiding library for character creation
from dataclasses import dataclass, field

@dataclass
class Character:
    name: str
    background: str
    level: int = 1
    xp: int = 0
    hp: int = 100
    inventory: list = field(default_factory=list)

# character = Character(
#     name="Sarhl Ender", 
#     background="Foreigner"
# )

# print(character)