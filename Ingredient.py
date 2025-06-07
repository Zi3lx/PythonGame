from dataclasses import dataclass
from Constants import *

@dataclass
class Ingredient:
    name: str
    color: tuple
    alcohol_content: float
    price: float
    image_path: str = ""
