import os
import pygame
from pygame import Vector2
from src.utils import utils

from src.utils.constants import *
from src.level import Level


class Player:
    ANIM_TIME = 10


    def __init__(self):
        """Initialize the player
        """
        # The tilemap position of the player
        self.position = Vector2(GRID_WIDTH / 2, GRID_HEIGHT / 2)
        self.move = Vector2(0)

        # Animation
        self.timer = self.ANIM_TIME
        self.image_index = 0

        # Load player images
        self.images = []
        directory = "assets/images/player/"

        for image_filename in os.listdir(directory):
            image = pygame.image.load(directory + image_filename)
            image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            self.images.append(image)

        # Items
        self.items = ["knijptang_placeholder", "heroine_placeholder"]
    
    
    def won(self) -> bool:
        """If the player has won

        Returns:
            bool: did the player win
        """
        return "fiets sleutel" in self.items


    def update(self, level: Level, key: int):
        """Update player

        Args:
            level (Level): the level
            key (int): key pressed
        """
        self.move = pygame.Vector2(0, 0)

        # Set the move according to the key pressed
        if key == pygame.K_w:
            self.move.y = -1
        elif key == pygame.K_s:
            self.move.y = 1
        elif key == pygame.K_d:
            self.move.x = 1
        elif key == pygame.K_a:
            self.move.x = -1

        new_position = self.position + self.move

        # Stop the player
        if new_position in level.current_room.walls:
            return
        elif new_position.x < 0 or new_position.x >= GRID_WIDTH or new_position.y < 0 or new_position.y >= GRID_HEIGHT:
            return

        # Get npc
        if npc := level.current_room.get_npc(new_position):
            if npc.has_item and npc.should_destroy:
                level.current_room.npcs.remove(npc)
                level.current_npc = None

                return
        
            level.current_npc = npc
            level.current_npc.get_line(self)
            npc.play_voiceline()
            
            return
        else:
            npc = level.current_npc
            if npc and npc.has_item and npc.should_destroy:
                level.current_room.npcs.remove(npc)

            level.current_npc = None

        # Check x position
        if new_position.x > GRID_WIDTH - 2 and level.move_room(1, 0):
            self.position.x = 1
            return
        elif new_position.x < 1 and level.move_room(-1, 0):
            self.position.x = GRID_WIDTH - 2
            return
        # Check y position
        elif new_position.y > GRID_HEIGHT - 2 and level.move_room(0, -1):
            self.position.y = 1
            return
        elif new_position.y < 1 and level.move_room(0, 1):
            self.position.y = GRID_HEIGHT - 2
            return

        self.position = new_position


    def draw(self, screen: pygame.Surface):
        """Draws the player to the screen

        Args:
            screen (pygame.Surface): the surface to draw on (always screen)
        """
        # Get the current image and rotate it
        image = self.images[self.image_index]
        image = pygame.transform.rotate(image, self.move.angle_to(Vector2(0)) - 90)

        # Draw the current image
        screen.blit(image, utils.convert_to_screen(self.position - Vector2(0.5)))

        # Change animation frame according to a timer
        if self.timer <= 0:
            self.image_index = 1 if self.image_index == 0 else 0
            self.timer = self.ANIM_TIME
        else:
            self.timer -= 1

