Shaker Module
=============

Moduł ``Shaker`` obsługuje logikę shakera, w którym gracz miesza składniki drinka.

Klasy
-----

Shaker
~~~~~~

.. py:class:: Shaker(x: int, y: int)

   Reprezentuje shaker – obiekt do mieszania składników drinków.

   :param x: Pozycja X shakera na ekranie.
   :param y: Pozycja Y shakera na ekranie.

   .. py:attribute:: contents
      :type: Dict[str, float]

      Aktualna zawartość shakera (nazwa składnika → ilość).

   .. py:attribute:: is_mixed
      :type: bool

      Czy shaker został wymieszany przynajmniej raz.

   .. py:attribute:: mixing_quality
      :type: float

      Jakość mieszania (0.5–1.0), wpływa na liczbę punktów.

   .. py:attribute:: overshaken
      :type: bool

      Czy gracz przesadził z mieszaniem.

   .. py:attribute:: shake_count
      :type: int

      Licznik liczby wstrząśnięć shakera.

   .. py:method:: add_ingredient(ingredient_name: str, amount: float = 0.008) -> bool

      Dodaje składnik do shakera. Jeśli brak miejsca – zwraca False.

   .. py:method:: clear()

      Resetuje zawartość shakera i przywraca wartości domyślne.

   .. py:method:: shake() -> bool

      Wstrząsa shakerem, zwiększa licznik i aktualizuje jakość mieszania.

   .. py:method:: update()

      Aktualizuje animację trzęsienia shakera.

   .. py:method:: get_normalized_contents() -> Dict[str, float]

      Zwraca składniki w proporcjach (suma = 1.0).

   .. py:method:: get_mixing_penalty() -> float

      Zwraca mnożnik punktów zależny od jakości mieszania.

   .. py:method:: draw(screen)

      Rysuje shaker, jego zawartość, status mieszania i pasek pojemności.

   .. py:method:: _get_mixed_color() -> Tuple[int, int, int]

      Zwraca uśredniony kolor zmieszanych składników.

   .. py:method:: _get_ingredient_color(ingredient_name: str) -> Tuple[int, int, int]

      Zwraca kolor przypisany konkretnemu składnikowi.
