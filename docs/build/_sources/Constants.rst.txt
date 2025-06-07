Constants Module
================

Moduł ``Constants`` zawiera stałe konfiguracyjne używane w grze, takie jak rozmiar ekranu, liczba klatek na sekundę (FPS) oraz podstawowe kolory w formacie RGB.

Stałe ogólne
------------

.. py:data:: SCREEN_WIDTH
   :type: int

   Szerokość okna gry w pikselach (1024 px).

.. py:data:: SCREEN_HEIGHT
   :type: int

   Wysokość okna gry w pikselach (768 px).

.. py:data:: FPS
   :type: int

   Liczba klatek na sekundę (60 FPS).

Paleta kolorów
--------------

Wszystkie kolory zapisane są jako krotki RGB (R, G, B):

.. py:data:: WHITE
   :type: tuple[int, int, int]

   Kolor biały ``(255, 255, 255)``

.. py:data:: BLACK
   Kolor czarny ``(0, 0, 0)``

.. py:data:: RED
   Kolor czerwony ``(255, 0, 0)``

.. py:data:: GREEN
   Kolor zielony ``(0, 255, 0)``

.. py:data:: BLUE
   Kolor niebieski ``(0, 0, 255)``

.. py:data:: YELLOW
   Kolor żółty ``(255, 255, 0)``

.. py:data:: ORANGE
   Kolor pomarańczowy ``(255, 165, 0)``

.. py:data:: PURPLE
   Kolor fioletowy ``(128, 0, 128)``

.. py:data:: BROWN
   Kolor brązowy ``(139, 69, 19)``

.. py:data:: GRAY
   Kolor szary ``(128, 128, 128)``

.. py:data:: DARK_GREEN
   Kolor ciemnozielony ``(0, 128, 0)``

.. py:data:: PINK
   Kolor różowy ``(255, 192, 203)``

.. py:data:: LIGHT_GRAY
   Jasny szary ``(200, 200, 200)``
