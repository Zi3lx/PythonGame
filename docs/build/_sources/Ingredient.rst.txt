Ingredient Module
=================

Moduł ``Ingredient`` zawiera definicję struktury danych reprezentującej pojedynczy składnik drinka.

Klasy
-----

.. py:class:: Ingredient(name, color, alcohol_content, price, image_path="")

   Reprezentuje składnik używany do tworzenia drinków (np. alkohol, sok, napój gazowany).

   :param name: Nazwa składnika (np. "Wódka").
   :type name: str

   :param color: Kolor składnika jako krotka RGB (np. (255, 255, 255)).
   :type color: tuple[int, int, int]

   :param alcohol_content: Zawartość alkoholu w składniku (np. 40.0 dla 40%).
   :type alcohol_content: float

   :param price: Cena jednostkowa składnika (np. 5.0).
   :type price: float

   :param image_path: (Opcjonalnie) Ścieżka do obrazka reprezentującego składnik.
   :type image_path: str
   :default: ""

   .. py:attribute:: name
      Nazwa składnika.

   .. py:attribute:: color
      Kolor składnika w formacie RGB.

   .. py:attribute:: alcohol_content
      Zawartość alkoholu w procentach (0.0–100.0).

   .. py:attribute:: price
      Cena jednostkowa składnika.

   .. py:attribute:: image_path
      Ścieżka do pliku graficznego (np. obrazek butelki).
