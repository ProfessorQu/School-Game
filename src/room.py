class Room:
    def __init__(self, x, y, walls) -> None:
        """Initialize Room

        Args:
            x (int): the x position of the room in the level
            y (int): the y position of the room in the level
            walls (List[Vector2]): the list of walls in the level
        """
        self.x = x
        self.y = y

        self.walls = walls
