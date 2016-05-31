"""
Defines Level class
"""

import pygame

import constants
import block

class Level():

  # List of sprites used in all levels.
  # Add or remove lists as needed for the game.
  block_list = None
  outline_list = None

  def __init__(self, player):
    self.block_list = pygame.sprite.Group()
    self.outline_list = pygame.sprite.Group()
    self.player = player


  # Update everything on this level
  def update(self):
    self.block_list.update()
    self.outline_list.update()

  def draw(self, screen):
    # Draw screen for current level
    screen.fill(constants.BLACK)

    # Draw all the sprite lists that we have
    self.outline_list.draw(screen)
    self.block_list.draw(screen)


# Define levels
class Level_1(Level):

  # Create level 1
  def __init__(self, player):
    Level.__init__(self, player)
    b_width = 70
    b_height = 32

    # Array with type of blocks
    level = []
    # Blocks for each row
    for x_idx in range(9):
      pos = [constants.LIGHT_GREEN, 85 + (b_width * x_idx), b_width + (b_height * 1)]
      level.append(pos)

    for x_idx in range(8):
      x_padding = 35
      pos = [constants.DARK_GREEN, 85 + (b_width * x_idx) + x_padding, b_width + (b_height * 2)]
      level.append(pos)

    for x_idx in range(9):
      pos = [constants.LIGHT_GREEN, 85 + (b_width * x_idx), b_width + (b_height * 3)]
      level.append(pos)

    for x_idx in range(6):
      x_padding = 105
      pos = [constants.DARK_GREEN, 85 + (b_width * x_idx) + x_padding, b_width + (b_height * 4)]
      level.append(pos)

    # Go through the level array and add blocks
    for element in level:
      outline = block.Block(constants.BLACK, b_width, b_height)
      outline.rect.x = element[1] - 1.5
      outline.rect.y = element[2] - 1.5
      self.outline_list.add(outline)
      b = block.Block(element[0], b_width-3, b_height-3)
      b.rect.x = element[1]
      b.rect.y = element[2]
      self.block_list.add(b)
