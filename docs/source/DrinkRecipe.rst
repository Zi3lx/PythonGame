DrinkRecipe Module
==================

Moduł ``DrinkRecipe`` zawiera definicję struktury danych reprezentującej przepis na drink.

Klasy
-----

.. py:class:: DrinkRecipe

   Reprezentuje jeden przepis na drink.

   .. py:attribute:: name
      :type: str

      Nazwa drinka.

   .. py:attribute:: ingredients
      :type: Dict[str, float]

      Składniki drinka w formacie: ``nazwa składnika → proporcja`` (wartość od 0.0 do 1.0). Wszystkie proporcje powinny sumować się do 1.0.

   .. py:attribute:: difficulty
      :type: int

      Poziom trudności przygotowania drinka (np. skala od 1 do 5).

   .. py:attribute:: base_points
      :type: int

      Bazowa liczba punktów przyznawana za dobrze wykonany drink.

   .. py:attribute:: description
      :type: str
      :default: ""

      Opcjonalny opis drinka wyświetlany graczowi.
