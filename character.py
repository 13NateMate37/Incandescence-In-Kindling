# Aiding library for character creation
from dataclasses import dataclass

@dataclass
class Character:
    name: str
    race: str
    level: int = 1
    xp: int = 0
    hp: int = 100
    inventory: list = field(default_factory=list)

