DrinksDB Module
===============

Moduł ``DrinksDB`` zawiera funkcje do inicjalizacji składników oraz gotowych przepisów na drinki, które wykorzystywane są w grze.

Import:

.. code-block:: python

   from DrinksDB import get_ingredients, get_drink_recipes

Funkcje
-------

.. py:function:: get_ingredients() -> List[Ingredient]

   Zwraca listę dostępnych składników do przygotowywania drinków.

   Każdy składnik to obiekt klasy :class:`Ingredient`, zawierający m.in. nazwę, kolor, procent alkoholu, koszt i ścieżkę do pliku graficznego.

   :return: Lista obiektów `Ingredient`.
   :rtype: List[Ingredient]


.. py:function:: get_drink_recipes() -> List[DrinkRecipe]

   Zwraca listę przepisów na znane drinki.

   Każdy przepis to obiekt klasy :class:`DrinkRecipe`, zawierający proporcje składników, poziom trudności, liczbę punktów oraz opis.

   :return: Lista obiektów `DrinkRecipe`.
   :rtype: List[DrinkRecipe]
