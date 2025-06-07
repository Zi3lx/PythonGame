IngredientBottle Module
=======================

Moduł ``IngredientBottle`` zawiera klasę reprezentującą butelkę ze składnikiem w grze. Każda butelka może być rysowana, obsługuje interakcje myszy i pozwala na nalewanie składników do shakera.

Klasy
-----

IngredientBottle
~~~~~~~~~~~~~~~~

.. py:class:: IngredientBottle(ingredient, x, y)

   Reprezentuje interaktywną butelkę zawierającą składnik (np. wódkę, sok) na ekranie gry.

   :param ingredient: Obiekt składnika, który reprezentuje zawartość butelki.
   :type ingredient: Ingredient

   :param x: Pozycja X butelki na ekranie.
   :type x: int

   :param y: Pozycja Y butelki na ekranie.
   :type y: int

   .. py:attribute:: ingredient
      :type: Ingredient

      Składnik przypisany do tej butelki.

   .. py:attribute:: rect
      :type: pygame.Rect

      Obszar kolizji (i rysowania) butelki.

   .. py:attribute:: is_pouring
      :type: bool

      Czy aktualnie butelka nalewa składnik.

   .. py:attribute:: font
      :type: pygame.font.Font

      Czcionka do renderowania nazw składników.

   .. py:attribute:: pour_rate
      :type: float

      Ilość składnika nalewana w jednym klatce gry (np. 0.008 jednostki na frame).

   .. py:attribute:: mouse_held
      :type: bool

      Czy gracz trzyma przycisk myszy na butelce.

   .. py:method:: draw(screen, ingredient_images)

      Rysuje butelkę składnika na ekranie. Używa obrazka z `ingredient_images`, jeśli jest dostępny, w przeciwnym razie rysuje kolorowy prostokąt.

      :param screen: Powierzchnia `pygame.Surface`, na której rysowana jest butelka.
      :type screen: pygame.Surface

      :param ingredient_images: Słownik mapujący nazwę składnika na obrazek.
      :type ingredient_images: Dict[str, pygame.Surface]

   .. py:method:: handle_event(event, mouse_pos)

      Obsługuje kliknięcia myszy i wykrywa, czy gracz trzyma przycisk nad tą butelką.

      :param event: Zdarzenie z systemu Pygame.
      :type event: pygame.event.Event

      :param mouse_pos: Aktualna pozycja kursora myszy.
      :type mouse_pos: Tuple[int, int]

      :return: `True` jeśli nalewanie jest aktywne, inaczej `False`.
      :rtype: bool
