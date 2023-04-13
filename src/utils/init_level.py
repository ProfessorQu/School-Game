from pygame import Vector2
from src.level import Level
from src.npc import NPC
from src.room import Room
from src.utils.constants import *


def init_level() -> Level:
    return Level(
        [
            Room(0, 0, True, True, False, True, [],
                [
                    NPC(10, 7, "Fiets",
                            "okselhaar",
                            "Joost stinkt",
                            "Niemand gaat dit zien",
                            "Ik zag Joost ervandoor gaan met je fietssleutel.\nZoek de heroine! Loop naar links uit deze kamer\nom het te vinden!"
                    )
                ]
            ),
            Room(1, 0, False, False, False, True, [],
                [
                    NPC(5, 5, "Korné",
                            "heroine",
                            "deur sleutel",
                            "Geef die heroine maar, dan krijg jij de sleutel\nvan het informatica lokaal.",
                            "N-n-n-n nee! Je hebt niks.\nGeef me heroine! Geef, geef, geef!"
                    ),
                ]),
            Room(2, 0, False, True, True, False, [Vector2(8, 13), Vector2(6, 13)],
                [
                    NPC(7, 13, "Deur",
                            "deur sleutel",
                            None,
                            "De deur gaat open",
                            "De deur zit dicht",
                            True
                    ),
                    
                ]),
            Room(2, -1, True, False, False, True, [],
                [
                    NPC(7, 10, "Joost",
                            "knijptang",
                            "fiets sleutel",
                            "Nee! Hoe durf je?!\nStelen van je eigen informatica docent?!",
                            "Hallo, wat is er? Sleutel? Nee die ligt hier niet."
                    )
                ]),
            Room(3, -1, False, True, True, True, [],
                [
                    NPC(10, 5, "Concierge",
                            "knijptang_placeholder",
                            "knijptang",
                            "Houd de dief!",
                            "Houd de dief!"
                    )
                ]),
            Room(1, 1, True, True, True, False, [],
                [
                    NPC(7, 7, "Heroine",
                            "heroine_placeholder",
                            "heroine",
                            "HAHA NIEMAND GAAT DIT ZIEN!!!!!!!!!!!!!!!",
                            "Hahaha niemand gaat dit zien",
                            True
                    )
                ])
        ]
    )