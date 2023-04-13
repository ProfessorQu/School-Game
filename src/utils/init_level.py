from pygame import Vector2
from src.level import Level
from src.npc import NPC
from src.room import Room


def init_level() -> Level:
    return Level(
        [
            Room(0, 0, [Vector2(x, y) for x in range(5) for y in range(3)],
                [
                    NPC(5, 5, "Korné",
                            "heroine",
                            "deur sleutel",
                            "Geef die heroine maar, dan krijg jij de sleutel\nvan het informatica lokaal.",
                            "N-n-n-n nee! Je hebt niks.\nGeef me heroine! Geef, geef, geef!"
                    ),
                    NPC(10, 10, "Fiets",
                            "okselhaar",
                            "Joost stinkt",
                            "Niemand gaat dit zien",
                            "Zoek de heroine! Loop naar links uit deze kamer\nom het te vinden!"
                    )
                ]
            ),
            Room(1, 0, [Vector2(x, y) for x in range(10) for y in range(5)],
                [
                    NPC(7, 10, "Joost",
                            "knijptang",
                            "sleutel",
                            "Nee! Hoe durf je?!\nStelen van je eigen informatica docent?!",
                            "Hallo, wat is er? Sleutel? Nee die ligt hier niet."
                    ),
                    NPC(10, 5, "Concierge",
                            "knijptang_placeholder",
                            "knijptang",
                            "Houd de dief!",
                            "Houd de dief!"
                    )
                ]
            ),
            Room(2, 0, [Vector2(x, y) for x in range(15) for y in range(5)],
                [
                    NPC(10, 13, "Deur",
                            "deur sleutel",
                            None,
                            "De deur gaat open",
                            "De deur zit dicht",
                            True
                    ),
                    NPC(9, 5, "Heroine",
                            "heroine_placeholder",
                            "heroine",
                            "HAHA NIEMAND GAAT DIT ZIEN!!!!!!!!!!!!!!!",
                            "Hahaha niemand gaat dit zien",
                            True)
                ]),
            Room(1, 1, [Vector2(x, y) for x in range(15) for y in range(5)], [])
        ]
    )