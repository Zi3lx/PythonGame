PlayerNameInput Module
======================

Moduł ``PlayerNameInput`` udostępnia graficzny interfejs do wpisywania imienia gracza.

Klasy
-----

PlayerNameInput
~~~~~~~~~~~~~~~

.. py:class:: PlayerNameInput(x, y, width, height)

   Klasa obsługująca interaktywne pole tekstowe do wpisywania imienia gracza.

   :param x: Pozycja X pola wejściowego.
   :type x: int
   :param y: Pozycja Y pola wejściowego.
   :type y: int
   :param width: Szerokość pola.
   :type width: int
   :param height: Wysokość pola.
   :type height: int

   .. py:attribute:: rect
      Prostokąt definiujący obszar interakcji.

   .. py:attribute:: text
      Aktualnie wpisany tekst (imię gracza).

   .. py:attribute:: active
      Flaga aktywności (czy pole zostało kliknięte).

   .. py:attribute:: cursor_visible
      Czy kursor jest widoczny (miganie).

   .. py:attribute:: cursor_timer
      Licznik czasu do migania kursora.

   .. py:method:: handle_event(event) -> bool

      Obsługuje zdarzenia wejściowe Pygame (kliknięcie, klawiatura).

      :param event: Zdarzenie Pygame
      :return: True jeśli naciśnięto Enter, w przeciwnym razie False.

   .. py:method:: update()

      Aktualizuje stan kursora (miganie co 30 klatek).

   .. py:method:: draw(screen)

      Rysuje pole wejściowe wraz z tekstem i migającym kursorem.

      :param screen: Powierzchnia Pygame, na której rysujemy.
