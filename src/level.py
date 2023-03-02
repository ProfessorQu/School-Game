class Level:
    def __init__(self, rooms) -> None:
        """Initialize level

        Args:
            rooms (List[Room]): a list of rooms in this level
        """
        self.rooms = rooms

        self.current_room_x = 0
        self.current_room_y = 0

    def move_room(self, x, y):
        """Move the current room with an offset of x and y

        Args:
            x (int): the distance to move the room in the x-axis
            y (int): the distance to move the room in the y-axis
        """
        new_room_x = self.current_room_x + x
        new_room_y = self.current_room_y + y

        for room in self.rooms:
            if room.x == new_room_x and room.y == new_room_y:
                self.current_room_x = new_room_x
                self.current_room_y = new_room_y

                break

    @property
    def current_room(self):
        """Get the current room

        Raises:
            ValueError: If there is no room with the current index

        Returns:
            Room: the current room
        """
        for room in self.rooms:
            if room.x == self.current_room_x and room.y == self.current_room_y:
                return room

        raise ValueError(
            f"X: {self.current_room_x}, Y: {self.current_room_y} are not rooms")
