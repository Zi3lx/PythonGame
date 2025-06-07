from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple


@dataclass
class DrinkRecipe:
    name: str
    ingredients: Dict[str, float]  # nazwa składnika -> ilość (0-1)
    difficulty: int
    base_points: int
    description: str = ""
