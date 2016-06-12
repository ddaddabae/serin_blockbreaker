"""
This module defines Player class.
The Player represents the user-controlled sprite on the screen.
"""

import pygame
import constants

class Player(pygame.sprite.Sprite):
  level = None

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    # Create an image of a bar, and fill it with a color
    width = 95
    height = 7
    self.image = pygame.Surface([width, height])
    self.image.fill(constants.LIGHT_GRAY)

    # Set a reference to the image rect
    self.rect = self.image.get_rect()
    self.rect.y = constants.SCREEN_HEIGHT - 20

    # Set speed vector of player
    self.change_x = 0
 

  def update(self):
    # Move left/right
    self.rect.x += self.change_x
    if self.rect.x <= 0:
      self.rect.x = 0
    elif self.rect.x >= constants.SCREEN_WIDTH - self.rect.width:
      self.rect.x = constants.SCREEN_WIDTH - self.rect.width

  def move_left(self):
    # When the user hits the left arrow
    self.change_x = -6
  
  def move_right(self):
    # When the user hits the right arrow
    self.change_x = 6

  def stop(self):
    # When the user turn off the keyboard
    self.change_x = 0
