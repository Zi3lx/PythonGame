Button Module
=============

Moduł ``Button`` zawiera klasę `Button`, która reprezentuje prosty przycisk w interfejsie graficznym opartym o Pygame. Przyciski mogą być rysowane na ekranie, reagują na najechanie kursora oraz kliknięcia.

Import:

.. code-block:: python

   from Button import Button

Klasy
-----

Button
~~~~~~

.. class:: Button(x, y, width, height, text, color=GRAY)

   Reprezentuje klikany przycisk interfejsu użytkownika w Pygame.

   :param x: Pozycja X lewego górnego rogu przycisku.
   :type x: int
   :param y: Pozycja Y lewego górnego rogu przycisku.
   :type y: int
   :param width: Szerokość przycisku.
   :type width: int
   :param height: Wysokość przycisku.
   :type height: int
   :param text: Tekst wyświetlany na przycisku.
   :type text: str
   :param color: Kolor tła przycisku w formacie RGB. Domyślnie ``GRAY``.
   :type color: tuple

   .. attribute:: rect

      Obiekt `pygame.Rect` określający pozycję i wymiary przycisku.

   .. attribute:: text

      Tekst wyświetlany na przycisku.

   .. attribute:: color

      Kolor przycisku jako krotka RGB.

   .. attribute:: is_hovered

      Flaga logiczna wskazująca, czy mysz znajduje się nad przyciskiem.

   .. method:: draw(screen)

      Rysuje przycisk na podanej powierzchni.

      :param screen: Powierzchnia `pygame.Surface`, na której rysowany jest przycisk.
      :type screen: pygame.Surface

   .. method:: handle_event(event)

      Obsługuje zdarzenia myszy (najechanie, kliknięcie).

      :param event: Obiekt zdarzenia `pygame.event.Event`.
      :type event: pygame.event.Event
      :returns: `True` jeśli przycisk został kliknięty, inaczej `False`.
      :rtype: bool
