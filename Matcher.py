from typing import List, Dict, Optional, Tuple
from DrinkRecipe import DrinkRecipe

class DrinkMatcher:
    def __init__(self, drink_database: List[DrinkRecipe]):
        self.database = drink_database

    def find_best_match(self, player_drink: Dict[str, float]) -> Tuple[Optional[DrinkRecipe], float, int]:
        """
        Znajduje najlepiej pasujący drink z bazy i oblicza podobieństwo.
        Zwraca: (najlepszy_drink, podobieństwo_0-1, punkty)
        """
        if not player_drink:
            return None, 0.0, 0

        best_match = None
        best_similarity = 0.0
        best_points = 0

        for recipe in self.database:
            similarity = self._calculate_similarity(player_drink, recipe.ingredients)

            if similarity > best_similarity:
                best_similarity = similarity
                best_match = recipe
                # Punkty = bazowe punkty * podobieństwo^2 (karze małe podobieństwa)
                best_points = int(recipe.base_points * (similarity ** 1.5))

        return best_match, best_similarity, best_points

    def _calculate_similarity(self, drink1: Dict[str, float], drink2: Dict[str, float]) -> float:
        """Oblicza podobieństwo między dwoma drinkami (0-1)"""
        all_ingredients = set(drink1.keys()) | set(drink2.keys())

        if not all_ingredients:
            return 0.0

        total_difference = 0.0

        for ingredient in all_ingredients:
            amount1 = drink1.get(ingredient, 0.0)
            amount2 = drink2.get(ingredient, 0.0)

            # Różnica bezwzględna
            difference = abs(amount1 - amount2)
            total_difference += difference

        # Maksymalna możliwa różnica to 2.0 (jeden ma 100%, drugi 0% wszystkich składników)
        # Podobieństwo = 1 - (średnia różnica / 2)
        similarity = 1.0 - (total_difference / 2.0)
        return max(0.0, similarity)