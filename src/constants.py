from pygame import Vector2

TILE_SIZE = 50

GRID_HEIGHT = 10
GRID_WIDTH = 20

SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE

ROOM1 = [
    Vector2(x, y) for x in range(5) for y in range(3)
]

ROOM2 = [
    Vector2(x, y) for x in range(10) for y in range(3, 5)
]
