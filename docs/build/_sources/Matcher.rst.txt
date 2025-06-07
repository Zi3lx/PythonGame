DrinkMatcher Module
===================

Moduł ``DrinkMatcher`` odpowiada za ocenę podobieństwa stworzonego przez gracza drinka do znanych przepisów w grze.

Klasy
-----

DrinkMatcher
~~~~~~~~~~~~

.. py:class:: DrinkMatcher(drink_database)

   Porównuje skład drinka przygotowanego przez gracza z bazą przepisów i wybiera najlepsze dopasowanie.

   :param drink_database: Lista dostępnych przepisów na drinki.
   :type drink_database: List[DrinkRecipe]

   .. py:method:: find_best_match(player_drink)

      Znajduje najlepiej dopasowany przepis do stworzonego drinka.

      :param player_drink: Słownik ze składnikami i ich ilościami (od 0.0 do 1.0).
      :type player_drink: Dict[str, float]

      :return: Krotka (najlepszy_drink, podobieństwo, przyznane_punkty)
      :rtype: Tuple[Optional[DrinkRecipe], float, int]

      - **najlepszy_drink** – przepis najbardziej zbliżony do wykonanego drinka.
      - **podobieństwo** – wartość od 0.0 do 1.0 reprezentująca podobieństwo.
      - **punkty** – liczba przyznanych punktów (bazowe * podobieństwo^1.5)

   .. py:method:: _calculate_similarity(drink1, drink2)

      Prywatna metoda obliczająca podobieństwo dwóch drinków na podstawie ich składników.

      :param drink1: Pierwszy drink (zazwyczaj drink gracza).
      :type drink1: Dict[str, float]

      :param drink2: Drugi drink (zazwyczaj przepis).
      :type drink2: Dict[str, float]

      :return: Podobieństwo w zakresie [0.0, 1.0]
      :rtype: float
