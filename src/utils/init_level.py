from pygame import Vector2
from src.level import Level
from src.npc import NPC
from src.room import Room
from src.utils.dialogue import Dialogue, Line

def init_level() -> Level:
    return Level(
        [
            Room(0, 0, [Vector2(x, y) for x in range(5) for y in range(3)],
                [
                    NPC(5, 5, "Korné",
                            "heroine",
                            "knijptang",
                            "Geef die heroine maar, dan krijg jij de sleutel\nvan het informatica lokaal.",
                            "N-n-n-n nee! Je hebt niks.\nGeef me heroine! Geef, geef, geef!"
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
                    )
                ]
            ),
            Room(2, 0, [Vector2(x, y) for x in range(15) for y in range(5)], []),
            Room(1, 1, [Vector2(x, y) for x in range(15) for y in range(5)], [])
        ]
    )