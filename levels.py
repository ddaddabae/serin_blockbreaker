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
  inner_list = None

  def __init__(self, player):
    self.block_list = pygame.sprite.Group()
    self.outline_list = pygame.sprite.Group()
    self.inner_list = pygame.sprite.Group()
    self.player = player


  # Update everything on this level
  def update(self):
    self.block_list.update()
    self.outline_list.update()
    self.inner_list.update()

  def draw(self, screen):
    # Draw screen for current level
    screen.fill(constants.BLACK)

    # Draw all the sprite lists that we have
    self.outline_list.draw(screen)
    self.block_list.draw(screen)
    self.inner_list.draw(screen)


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

# Define levels
class Level_2(Level):

  # Create level 2
  def __init__(self, player):
    Level.__init__(self, player)
    b_width = 70
    b_height = 32

    # Array with type of blocks
    level = []
    hard_level = []
    # Blocks for each row
    for x_idx in range(8):
      x_padding = 35
      pos = [constants.WHITE_GREEN, 85 + (b_width * x_idx) + x_padding, b_width + (b_height * 1)]
      level.append(pos)

    for x_idx in range(6):
      x_padding = 105
      pos = [constants.LIGHT_BLUE, 85 + (b_width * x_idx) + x_padding, b_width + (b_height * 2)]
      hard_level.append(pos)

    for x_idx in range(9):
      pos = [constants.WHITE_GREEN, 85 + (b_width * x_idx), b_width + (b_height * 3)]
      level.append(pos)

    for x_idx in range(8):
      x_padding = 35
      pos = [constants.LIGHT_BLUE, 85 + (b_width * x_idx) + x_padding, b_width + (b_height * 4)]
      hard_level.append(pos)

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

    for element in hard_level:
      outline = block.Block(constants.BLACK, b_width, b_height)
      outline.rect.x = element[1] - 1.5
      outline.rect.y = element[2] - 1.5
      self.outline_list.add(outline)
      b = block.HardBlock(element[0], b_width-3, b_height-3, 2)
      b.rect.x = element[1]
      b.rect.y = element[2]
      b.inner = block.Block(constants.WHITE_BLUE, b_width-10, b_height-10)
      b.inner.rect.x = element[1]+4
      b.inner.rect.y = element[2]+4
      self.block_list.add(b)
      self.inner_list.add(b.inner)
