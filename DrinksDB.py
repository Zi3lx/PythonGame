from Ingredient import Ingredient
from DrinkRecipe import DrinkRecipe
from Constants import *

def get_ingredients():
    return [
        Ingredient("Wódka", WHITE, 40.0, 10, "assets/wodka.jpg"),
        Ingredient("Rum", BROWN, 37.5, 12, "assets/rum.jpg"),
        Ingredient("Whiskey", ORANGE, 40.0, 15, "assets/whiskey.jpg"),
        Ingredient("Gin", WHITE, 37.5, 11, "assets/gin.jpg"),
        Ingredient("Sok pomarańczowy", ORANGE, 0.0, 3, "assets/sok_pom.jpg"),
        Ingredient("Sok żurawinowy", RED, 0.0, 4, "assets/sok_zur.jpg"),
        Ingredient("Lemoniada", YELLOW, 0.0, 2, "assets/lemoniada.jpg"),
        Ingredient("Cola", BLACK, 0.0, 2, "assets/cola.jpg"),
        Ingredient("Grenadina", RED, 0.0, 5, "assets/grenadina.jpg"),
        Ingredient("Wermut", DARK_GREEN, 15.0, 8, "assets/wermut.jpg"),
        Ingredient("Sprite", WHITE, 0.0, 2, "assets/sprite.jpg"),
        Ingredient("Sok ananasowy", YELLOW, 0.0, 3, "assets/sok_anansowy.jpg")
    ]

def get_drink_recipes():
    return [
        # Proste drinki
        DrinkRecipe("Screwdriver", {"Wódka": 0.6, "Sok pomarańczowy": 0.4}, 1, 100, "Wódka z sokiem pomarańczowym"),
        DrinkRecipe("Cuba Libre", {"Rum": 0.4, "Cola": 0.5, "Lemoniada": 0.1}, 1, 120, "Rum z colą i cytryną"),
        DrinkRecipe("Whiskey Cola", {"Whiskey": 0.4, "Cola": 0.6}, 1, 110, "Klasyka - whiskey z colą"),
        DrinkRecipe("Gin Tonic", {"Gin": 0.4, "Sprite": 0.6}, 1, 115, "Orzeźwiający gin z tonikiem"),
        DrinkRecipe("Rum & Juice", {"Rum": 0.5, "Sok ananasowy": 0.5}, 1, 105, "Tropikalny rum z sokiem"),

        # Średnie drinki
        DrinkRecipe("Cosmopolitan", {"Wódka": 0.4, "Sok żurawinowy": 0.3, "Lemoniada": 0.2, "Grenadina": 0.1}, 2,
                    200, "Różowy klasyk"),
        DrinkRecipe("Martini", {"Gin": 0.7, "Wermut": 0.3}, 2, 180, "Elegancki gin martini"),
        DrinkRecipe("Vodka Martini", {"Wódka": 0.7, "Wermut": 0.3}, 2, 175, "Wódczana wersja martini"),
        DrinkRecipe("Sea Breeze", {"Wódka": 0.3, "Sok żurawinowy": 0.4, "Sok ananasowy": 0.3}, 2, 190,
                    "Orzeźwiający drink"),
        DrinkRecipe("Bahama Mama", {"Rum": 0.4, "Sok ananasowy": 0.3, "Grenadina": 0.2, "Sprite": 0.1}, 2, 210,
                    "Tropikalny koktajl"),

        # Złożone drinki
        DrinkRecipe("Long Island", {"Wódka": 0.2, "Rum": 0.2, "Gin": 0.2, "Cola": 0.3, "Lemoniada": 0.1}, 3, 300,
                    "Silny mix alkoholi"),
        DrinkRecipe("AMF", {"Wódka": 0.2, "Rum": 0.2, "Gin": 0.2, "Sprite": 0.3, "Grenadina": 0.1}, 3, 320,
                    "Adios Mother F***er"),
        DrinkRecipe("Zombie", {"Rum": 0.6, "Sok ananasowy": 0.2, "Grenadina": 0.1, "Lemoniada": 0.1}, 3, 280,
                    "Mocny rum drink"),
        DrinkRecipe("Hurricane", {"Rum": 0.4, "Sok ananasowy": 0.3, "Sok żurawinowy": 0.2, "Grenadina": 0.1}, 3,
                    290, "Niszczący huragan"),

        # Eksperymenty
        DrinkRecipe("Mystery Mix", {"Wódka": 0.25, "Rum": 0.25, "Sok pomarańczowy": 0.25, "Sprite": 0.25}, 2, 250,
                    "Tajemniczy mix"),
        DrinkRecipe("Rainbow", {"Grenadina": 0.3, "Sok ananasowy": 0.3, "Sprite": 0.2, "Wódka": 0.2}, 2, 220,
                    "Kolorowy drink")
    ]