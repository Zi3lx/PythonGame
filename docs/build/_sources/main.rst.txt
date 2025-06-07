BartenderGame Module
====================

Moduł ``main`` zawiera główną klasę gry "Polej Mi". Obsługuje wszystkie etapy gry:
menu, mieszanie drinków, porównywanie ich do przepisów oraz wynik.

GameState
---------

.. py:class:: GameState

   Wyliczenie reprezentujące stan gry:

   - ``MENU``: Ekran startowy
   - ``PLAYING``: Gra w toku
   - ``RESULT``: Wyświetlanie wyniku
   - ``PAUSE``: Pauza (niewykorzystane)
   - ``NAME_INPUT``: Ekran wprowadzania imienia

BartenderGame
-------------

.. py:class:: BartenderGame

   Główna klasa sterująca grą. Obsługuje logikę UI, przetwarzanie zdarzeń, obsługę gracza, nalewanie, mieszanie i ocenianie drinków.

   .. py:method:: __init__()
      Inicjalizuje wszystkie elementy gry, ładowanie zasobów, UI i stany.

   .. py:method:: run()
      Uruchamia główną pętlę gry.

   .. py:method:: handle_events() -> bool
      Obsługuje zdarzenia Pygame: kliknięcia, wpisywanie imienia, przejścia między ekranami.
      Zwraca False, jeśli użytkownik zamknął grę.

   .. py:method:: update()
      Aktualizuje stan gry i nalewania.

   .. py:method:: draw_menu()
      Rysuje ekran menu (powitanie, opis, rekordy, przyciski).

   .. py:method:: draw_game()
      Rysuje ekran gry: butelki, shaker, przyciski i instrukcje.

   .. py:method:: draw_result()
      Rysuje ekran z wynikiem drinka: podobieństwo, punkty, analiza.

   .. py:method:: serve_drink()
      Porównuje aktualny drink z przepisami i wylicza wynik.

   .. py:method:: save_scores()
      Zapisuje rekordy do pliku JSON w formacie: ``[ {"name": ..., "score": ..., "drinks": ...} ]``.

   .. py:method:: load_scores() -> List[dict]
      Wczytuje rekordy z pliku JSON. Obsługuje zarówno nowy, jak i stary format (same liczby).

   .. py:attribute:: ingredient_bottles
      Lista butelek (obiektów klasy IngredientBottle).

   .. py:attribute:: ingredient_images
      Mapowanie: nazwa -> obrazek butelki.

   .. py:attribute:: shaker
      Obiekt shakera do mieszania drinków.

   .. py:attribute:: drink_matcher
      Obiekt dopasowujący drinki gracza do znanych przepisów.

   .. py:attribute:: high_scores
      Lista najlepszych wyników gracza.

   .. py:attribute:: player_name
      Imię wprowadzone przez gracza.

   .. py:attribute:: score
      Aktualna liczba punktów gracza.

   .. py:attribute:: last_result
      Wynik ostatnio podanego drinka (słownik: match, similarity, points itd.).

   .. py:attribute:: state
      Aktualny stan gry (typ GameState).

   .. py:attribute:: name_input
      Obiekt wejścia tekstowego dla imienia gracza.

   .. py:attribute:: shake_button, serve_button, clear_button, menu_button
      Przyciski na ekranie gry.

   .. py:attribute:: start_button, quit_button, confirm_name_button
      Przyciski na ekranie menu.
