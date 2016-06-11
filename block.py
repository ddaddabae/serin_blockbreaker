"""
Define Block class
"""
import pygame
import constants

class Block(pygame.sprite.Sprite):

  def __init__(self, color, width, height):
    pygame.sprite.Sprite.__init__(self)

    # Create an image of the block, and fill it with a color.
    self.image = pygame.Surface([width, height])
    self.image.fill(color)

    # Set a reference to the image rect
    self.rect = self.image.get_rect()

    # Instance variables that control the edges of where we bounce 
    self.left_boundary = 0
    self.right_boundary = 0
    self.top_boundary = 0
    self.bottom_boundary = 0

    # Instance varables for our current speed and direction
    self.change_x = 0
    self.change_y = 0


class HardBlock(Block):

  def __init__(self, color, width, height, max_collision):
    Block.__init__(self, color, width, height)
    self.collision_count = max_collision

