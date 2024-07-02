import pygame
from pygame.sprite import Sprite
from random import randint  # Import randint from random module

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()  # Initialize the Sprite class
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp').convert()
        self.image.set_colorkey((255, 255, 255))  # Set white color as transparent
        self.image.fill((0, 255, 0), special_flags=pygame.BLEND_MULT)  # Tint with green color
        self.rect = self.image.get_rect()

        # Generate random starting positions
        self.rect.x = randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = randint(0, self.settings.screen_height - self.rect.height)

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False

    def update(self):
        """Move the alien horizontally"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
